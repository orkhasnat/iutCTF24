from hashlib import md5
from Crypto.Util.number import getPrime
from random import randint

def getParams():
    q = getPrime(512)
    k = randint(1, q - 1)
    g = randint(1, q - 1)
    r = pow(g, k, q)
    return q, k, r

def sign(m, q, k, r, d):
    h = int(md5(m.encode()).hexdigest(), 16)
    s = (h + r * d) % q
    s = (s * pow(k, -1, q)) % q
    return s


q, k, r = getParams()
d = int(open('flag.txt', 'rb').read().hex(), 16)

s1 = sign('play_station_three', q, k, r, d)
s2 = sign('jail_break', q, k, r, d)

with open('out.txt', 'w') as f:
    f.write(f'q = {q}\n')
    f.write(f'r = {r}\n')
    f.write(f's1 = {s1}\n')
    f.write(f's2 = {s2}')