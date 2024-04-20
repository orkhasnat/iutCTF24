import pyqrcode as QR
from PIL import Image, ImageFilter

flag = "iutctf{4_u_blurr1ng_15n7_an_1ssu3_15_17?}"

img = QR.create(flag)
img.png("../chal.png", scale=10)

img = Image.open("../chal.png")

img = img.convert("L")
# print(img.mode)
blur = img.filter(ImageFilter.GaussianBlur(radius=7))
blur.save("../chal.png")