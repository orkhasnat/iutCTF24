from PIL import Image


def hide(file, data):
  img = Image.open(file)
  if img.mode != 'RGBA':
    img = img.convert('RGBA')

  data_bytes = data.encode('utf-8')
  r, g, b, a = img.split()
  alpha_data = list(a.getdata())

  byte_index = 0
  bit_index = 0

  for col in range(img.width):
    for row in range(img.height):
      if byte_index < len(data_bytes):
        byte = data_bytes[byte_index]
        bit = (byte >> bit_index) & 1
        alpha_data[col + row * img.width] = (alpha_data[col + row * img.width]
                                             & 0xFE) | bit
        bit_index += 1
        if bit_index >= 8:
          bit_index = 0
          byte_index += 1
      else:
        break

  a.putdata(alpha_data)
  img = Image.merge("RGBA", (r, g, b, a))
  img.save('../chal.png')


flag = "iutctf{bruh_7h47_w45_345y}"
hide('og.png', flag[::-1])
