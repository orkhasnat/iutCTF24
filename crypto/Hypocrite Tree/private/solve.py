from tqdm import tqdm

io = ProcessWrapper(['python', '/content/server.py'])

io.recvline()
l = io.recvline().strip().split()
s, h = bytes.fromhex(l[3].replace(',', '')), l[-1]


def get_blocks(s):
  blocks = []
  for i in range(0, len(s), 8):
      blocks.append(s[i: i + 8])
  return blocks


def make_pairs(blocks):
  pairs = []
  for i in range(0, len(blocks), 2):
    pairs.append([blocks[i], blocks[i + 1]])
  return pairs


pairs = make_pairs(get_blocks(s))
n = len(pairs)

for mask in tqdm(range(1, 1 << n)):
  to_send = b''
  for i, pair in enumerate(pairs):
    if (mask & (1 << i)):
      to_send += pair[1]
      to_send += pair[0]
    else:
      to_send += pair[0]
      to_send += pair[1]

  io.recvuntil(': ')
  io.sendline(to_send.hex())

for _ in range(5):
  print(io.recvline())
