from Crypto.Util.number import getPrime, bytes_to_long as b2l

with open('flag.txt', 'rb') as f:
    flag = f.read()

assert (len(flag) == 28)

p = getPrime(2048)
e = 16588

flag = b2l(flag)
ct = pow(flag, e, p)

with open('out.txt', 'w') as f:
    f.write(f'p = {p}\n')
    f.write(f'ct = {ct}')


