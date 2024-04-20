from tqdm import tqdm
import time

io = ProcessWrapper(['python', '/content/server.py'])

sofar = ''
pos = 0

io.recvline()

sz = 256
for _ in tqdm(range(sz)):
  io.recvuntil(': ')
  to_send = str(pos) + ' ' + sofar + 'a'
  io.sendline(to_send)
  start = time.time()
  io.recvline()
  T = time.time() - start

  if T <= 0.5:
    sofar += 'a'
  else:
    sofar += 'b'
  pos += 1

io.recvuntil(': ')
io.sendline(sofar)

print(io.recvline())