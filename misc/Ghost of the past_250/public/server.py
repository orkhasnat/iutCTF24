#!/usr/local/bin/python

import random
import hashlib

print('Welcome Welcome welcome. Want the flag? Predict my letters and you will get it!')

def get_word(sz):
    ret = ''
    for _ in range(sz):
        toss = random.randint(1, 10)
        if toss <= 5:
            ret += 'a'
        else:
            ret += 'b'
    return ret

def MD5(s):
    return int(hashlib.md5(s.encode()).hexdigest(), 16)

sz = 50
word = get_word(sz)
mod = int(1e9 + 7)

def process_query(p, s):
    global word
    minSum = 1<<2048
    st, ed = 0, len(s) - 1
    while ed < len(word) and ed <= p:
        s_ = word[st : ed + 1]
        Sum = abs(MD5(s) - MD5(s_))
        minSum  = min(minSum, Sum)
        st, ed = st + 1, ed + 1
    return (pow(minSum, 42069) % mod + random.randint(1<<254, 1<<256)) % mod

for _ in range(sz):
    q = input('Enter your query: ').split()
    p, s = int(q[0]), q[1]
    if len(s) > sz:
        print('What a dumb thing to ask!')
        exit()
    print('Here is your answer:', process_query(p, s))

predicted = input('Moment of truth. Enter your prediction: ')
if word == predicted:
    print(open('flag.txt', 'r').read())
else:
    print('Lo053r!')