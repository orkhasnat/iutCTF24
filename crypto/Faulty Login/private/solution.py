# pin = '98492256' 

def decrypt(s, key):
    key = key.encode('utf-8')
    decrypted = b''
    for i in range(0, len(s), len(key)):
        decrypted += bytes([s[(i+j)%len(s)] ^ key[j] for j in range(len(key))])
    return decrypted

encrypted_flag = b'PM@ZFTNx\tgy\t@\x01jn\tJk\n|qGoi\x0f\x05\t|O\\C'
partial_flag = 'iutctf{'

print(decrypt(encrypted_flag, partial_flag).decode()[:7]) #9849225

for i in range(10):
    pin = '9849225' + str(i)
    
    flag = decrypt(encrypted_flag, pin)
    print(pin)
    print(flag)

# 98492256
# b'iutctf{N0_M0r3_X0r_3NCrYP710N}iu'
