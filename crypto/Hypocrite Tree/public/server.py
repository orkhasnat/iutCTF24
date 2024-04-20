#!/usr/local/bin/python

from hashlib import sha256
import os

def get_blocks(s):
    blocks = []
    for i in range(0, len(s), 8):
        blocks.append(s[i : i + 8])
    return blocks

class HTREE:
    def __init__(self, s):
        self.blocks = get_blocks(s)

    def COMBINE(self, LH, RH):
        if int(LH.hex(), 16) > int(RH.hex(), 16):
            LH, RH = RH, LH
        return sha256(LH + RH).digest()
    
    def HASH(self, L, R):
        if L == R:
            return sha256(self.blocks[L]).digest()
        else:
            M = (L + R) // 2
            LH = self.HASH(L, M)
            RH = self.HASH(M + 1, R)
            return self.COMBINE(LH, RH)
        
    def GET(self):
        return self.HASH(0, len(self.blocks) - 1)
        

print('Welcome to the Hypocrite Tree. Show your different faces and pretend to be the same persona to get the flag!')

s = os.urandom(128)
T = HTREE(s)
h = T.GET()

seen = set()
seen.add(sha256(s).digest())

print(f'For the string {s.hex()}, the hypocrite hash is {h.hex()}')

for rounds in range(1, 256):
    s = bytes.fromhex(input('Enter your new face: '))
    assert len(s) == 128, "Make sure the string is of the correct length"
    assert sha256(s).digest() not in seen, "Too honset for the flag -_-"

    h_ = HTREE(s).GET()
    assert h == h_, "Too dumb for the flag -_-"
    print('Thats my lovely hypocrite boy!')

with open('flag.txt', 'r') as f:
    print(f.read())