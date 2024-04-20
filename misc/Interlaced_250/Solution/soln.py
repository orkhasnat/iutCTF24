from PIL import Image

i = Image.open("../chal.png")
w, h = i.size

ogh1 = h // 2
ogh2 = h - ogh1

i1 = Image.new("RGB", (w, ogh1))
i2 = Image.new("RGB", (w, ogh2))

for y in range(h):
  if y % 2 == 0:
    # even rows from i1
    row = i.crop((0, y, w, y + 1))
    i1.paste(row, (0, y // 2))
  else:
    # odd rows from i2
    row = i.crop((0, y, w, y + 1))
    i2.paste(row, (0, (y - 1) // 2))

i1.save("qr1.png")
i2.save("qr2.png")