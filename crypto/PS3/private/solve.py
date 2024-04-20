from hashlib import md5

h1 = int(md5(b'play_station_three').hexdigest(), 16)
h2 = int(md5(b'jail_break').hexdigest(), 16)

with open('out.txt', 'r') as f:
    exec(f.read())

l = ((h1 - h2 + q) * s2 * pow(s1-s2 + q, -1, q)) % q
l = (l - h2 + q) % q
d = (l * pow(r, -1, q)) % q
flag = d.to_bytes(512//8, 'big')
print(flag)