import json
from Crypto.Cipher import AES
from itertools import product
from tqdm import tqdm
from Crypto.Util.Padding import pad, unpad


def connect():
  io = ProcessWrapper(['python', '/content/server.py'])
  return io


def xor(sa, sb):
  return bytes([a ^ b for a, b in zip(sa, sb)])


def decrypt_data(enc_data, iv, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = cipher.decrypt(enc_data)
    return data


def encrypt_data(data, iv, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(data)
    return enc


def decrypt_ECB(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    data = cipher.decrypt(data)
    return unpad(data, 16)


opts = [str(i) for i in range(10)]
combs = list(product(opts, repeat=4))
KP = dict()

io = connect()

query_ct = io.recvline()
enc_flag = io.recvline()
enc_text = io.recvline()
enc_iv = io.recvline()

for comb in tqdm(combs):
  key = b'0' * 12 + ''.join(c for c in comb).encode()
  iv = xor(xor(b'lalalaaaalaalaa!', b'0123456789012345'), key)
  to_send = {
      "encrypted_pass": iv.hex() + query_ct,
      "data": b'symmetry is fun!'.hex(),
      "operation": 1
  }
  io.sendline(json.dumps(to_send))
  KP[bytes.fromhex(io.recvline())] = key

for comb in tqdm(combs):
  key = b'0' * 12 + ''.join(c for c in comb).encode()
  iv = xor(xor(b'lalalaaaalaalaa!', b'0123456789012345'), key)
  to_send = {
      "encrypted_pass": iv.hex() + query_ct,
      "data": enc_text,
      "operation": 2
  }
  io.sendline(json.dumps(to_send))
  inter = bytes.fromhex(io.recvline())

  if inter in KP:
    key2, key3 = KP[inter], key
    print('found!')

    priv_iv = decrypt_ECB(decrypt_ECB(bytes.fromhex(enc_iv), key3), key2)
    flag = decrypt_data(decrypt_data(
        bytes.fromhex(enc_flag), priv_iv, key3), priv_iv, key2)
    print(flag)
    break
