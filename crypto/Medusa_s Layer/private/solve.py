from Crypto.Util.number import GCD
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
from tqdm import tqdm

H_neg = int(hashlib.sha256(str(-1).encode()).hexdigest(), 16)
H_zero = int(hashlib.sha256(str(0).encode()).hexdigest(), 16)
H_one = int(hashlib.sha256(str(1).encode()).hexdigest(), 16)

def connect():
  io = ProcessWrapper(['python', '/content/server.py'])
  return io

def getRSAquery(io, m):
  io.recvuntil(': ')
  io.sendline('2')
  io.recvline()
  io.sendline(str(m))
  ret = int(io.recvline().strip().split('= ')[1], 16)
  return ret

def getHint(io, pos, ch):
  io.recvuntil(': ')
  io.sendline('1')
  io.recvuntil(': ')
  io.sendline(str(pos) + ' ' + str(ch))
  ret = int(io.recvline().strip().split('= ')[1], 16)
  return ret

def decryptAES(key, ct):
  cipher = AES.new(key, AES.MODE_ECB)
  pt = unpad(cipher.decrypt(ct), AES.block_size)
  return pt.decode()

def belongs_to(c, y, g, q):
  assert((q - 1) % 4 == 0)
  res = (q - 1) // 4
  y_ = pow(y, res, q)
  g_ = pow(g, res, q)
  for i in range(4):
    l = pow(g_, i, q)
    if l == y_ and i == c % 4:
      return True
  return False


def go(io):
  io.recvline()

  ct = bytes.fromhex(io.recvline().strip().split('= ')[1])
  e = int(io.recvline().strip().split('= ')[1], 16)
  g = int(io.recvline().strip().split('= ')[1], 16)
  q = int(io.recvline().strip().split('= ')[1], 16)

  if (q - 1) % 4 != 0: return False
  if pow(g, (q - 1) // 4, q) == 1: return False
  print('Hopeful!!')

  m1 = getRSAquery(io, 2)
  m2 = getRSAquery(io, 3)

  n = GCD(2**e - m1, 3**e - m2)
  for i in range(2, 100):
    while n % i == 0: n //= i

  global H_neg, H_zero, H_one

  c_neg = pow(H_neg, e, n)
  c_zero = pow(H_zero, e, n)
  c_one = pow(H_one, e, n)

  st = set([c_neg % 4, c_zero % 4, c_one % 4])
  if len(st) != 3: return False

  print('More hopeful!!')

  key = []

  for pos in tqdm(range(16)):
    lo, hi = 0, 255
    while lo <= hi:
      mid = (lo + hi) // 2
      hint = getHint(io, pos, mid)

      if belongs_to(c_zero, hint, g, q):
        print('Found ', mid)
        key.append(mid)
        break
      elif belongs_to(c_one, hint, g, q):
        lo = mid + 1
      elif belongs_to(c_neg, hint, g, q):
        hi = mid - 1
      else:
        print('This is not supposed to happen???')
        return False

  key = bytes(key)
  flag = decryptAES(key, ct)
  print(flag)
  return True

while True:
  print('Trying...')
  if go(connect()): break