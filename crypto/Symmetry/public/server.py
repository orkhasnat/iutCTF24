#!/usr/local/bin/python

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import random
import json

def get_key(sz):
    key = '0' * (16 - sz)
    for _ in range(sz):
        key += str(random.randint(0, 9))
    return key.encode()

key1 = get_random_bytes(16)
key2, key3 = get_key(4), get_key(4)

pub_iv = b'lalalaaaalaalaa!'
priv_iv = get_random_bytes(16)

flag = open('flag.txt', 'rb').read().strip()

def encrypt_data(data, iv, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(data)
    return enc

def decrypt_data(enc_data, iv, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = cipher.decrypt(enc_data)
    return data

def encrypt_ECB(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    data = cipher.encrypt(pad(data, 16))
    return data

query_ct = encrypt_data(b'0123456789012345', pub_iv, key1)
print(query_ct.hex())

enc_flag = encrypt_data(encrypt_data(flag, priv_iv, key2), priv_iv, key3)
print(enc_flag.hex())

enc_text = encrypt_data(encrypt_data(
    b'symmetry is fun!', priv_iv, key2), priv_iv, key3)
print(enc_text.hex())

enc_iv = encrypt_ECB(encrypt_ECB(priv_iv, key2), key3)
print(enc_iv.hex())

for _ in range(15000):
    query = json.loads(input())
    enc_pwd = bytes.fromhex(query["encrypted_pass"])
    data = bytes.fromhex(query["data"])
    opt = query["operation"]
    pwd = decrypt_data(enc_pwd[16:], enc_pwd[:16], key1)

    if opt == 1:
        print(encrypt_data(data, priv_iv, pwd).hex())
    elif opt == 2:
        print(decrypt_data(data, priv_iv, pwd).hex())
    else:
        print('Invalid operation')
        exit()
