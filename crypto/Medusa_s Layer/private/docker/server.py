#!/usr/local/bin/python

from random import randint
import hashlib
from binascii import hexlify
from Crypto.Cipher import AES
from Crypto.Util.number import getPrime, getStrongPrime, isPrime
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

print('Welcome to the layers of death. Only the bravest shall survive!')

def getLayer1(flag):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(pad(flag, AES.block_size))
    return key, ct

def getLayer2(sz):
    e = 65537
    p, q = getPrime(sz), getPrime(sz)
    return e, p * q

def getLayer3(sz):
    q = getStrongPrime(sz)
    g = randint(2, q - 1)
    return g, q

flag = open('flag.txt', 'rb').read()
key, ct = getLayer1(flag)
e, n = getLayer2(256)
g, q = getLayer3(1024)

print('ct = ', hexlify(ct).decode())
print('e = ', hex(e))
print('g = ', hex(g))
print('q = ', hex(q))

def get_hint(pos, ch):
    global e, n
    global g, q
    d = key[pos] - ch
    if d:
        d //= abs(d)
    h = int(hashlib.sha256(str(d).encode()).hexdigest(), 16)
    c = pow(h, e, n)
    for _ in range(100):
      bit = randint(2, c.bit_length() - 1)
      c = c ^ (1 << bit)
    hint = pow(g, c, q)
    return hint

queries = 130
while queries >= 1:
    print('Enter the type of query that you need(1 or 2):', end = ' ')
    o = int(input())
    if o == 1:
        print('Enter a position (0-15) and ascii value (0 - 255) of a character to get a hint :', end=' ')
        idx, ch = map(int, input().split())
        assert (idx < 16 and idx >= 0)
        hint = get_hint(idx, ch)
        print('hint = ', hex(hint))
    elif o == 2:
        print('Brave stranger, how may the oracle help you? ')
        p = int(input())
        assert(p.bit_length() < 128)
        answer = pow(p, e, n)
        print('answer = ', hex(answer))
    else:
        exit()
    queries -= 1

print('Bye. All queries finished. Hope Medusa didnt kill ya!!!')