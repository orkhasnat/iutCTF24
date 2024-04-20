import pyqrcode as QR
from PIL import Image

flag = "iutctf{r34lly_ju57_4_pr0gr4mm1ng_ch4ll3ng3!}"


def qr_gen():
  half = len(flag) // 2
  i1 = QR.create(flag[:half])
  i2 = QR.create(flag[half:])
  i1.png("p1.png", scale=8)
  i2.png("p2.png", scale=8)


def createChall():
  i1 = Image.open("p1.png")
  i2 = Image.open("p2.png")

  w1, h1 = i1.size
  w2, h2 = i2.size

  chall = Image.new("RGB", (w1, h1 + h2))

  for y in range(h1 + h2):
    # even rows from i1
    if y % 2 == 0:
      row = i1.crop((0, y // 2, w1, y // 2 + 1))
    # odd rows from i2
    else:
      row = i2.crop((0, y // 2, w1, y // 2 + 1))

    chall.paste(row, (0, y))

  chall.save("../chal.png")


qr_gen()
createChall()