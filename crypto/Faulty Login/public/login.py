from Crypto.Hash import SHA256
from Crypto.Util.number import long_to_bytes
from getpass import getpass
from .utils import check_user, check_flag

def hash_string(s):
    h = SHA256.new()
    h.update(s.encode())
    hash = h.hexdigest()
    return long_to_bytes(int(hash, 16))

username = input("Enter your username: ").strip()
pin = getpass("Enter your 8-digit pin: ").strip()

if not check_user(hash_string(username), hash_string(pin)):
    print("Invalid credentials. Exiting.")
    exit(1)

with open("private/flag.txt", 'r') as f:
    flag = f.read().strip()

if not check_flag(hash_string(flag)):
    print("Invalid flag. Exiting.")
    exit(1)

def encrypt(s, key):
    s = s.encode('utf-8')
    key = key.encode('utf-8')
    encrypted = b''
    for i in range(0, len(s), len(key)):
        encrypted += bytes([s[(i+j)%len(s)] ^ key[j] for j in range(len(key))])
    return encrypted

encrypted_flag = encrypt(flag, pin)
print("Here is the encrypted flag:", encrypted_flag)