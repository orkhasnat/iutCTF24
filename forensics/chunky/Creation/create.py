import zstandard
import zlib
PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'

def write_png_chunk(stream, chunk_type, chunk_data):
  crc = zlib.crc32(chunk_type + chunk_data)

  stream.write(encode_png_uint31(len(chunk_data)))
  stream.write(chunk_type)
  stream.write(chunk_data)
  stream.write(crc.to_bytes(4, "big"))


def encode_png_ihdr(
    width,
    height,
    bit_depth=8, 
    colour_type=2, 
    compression_method=1, 
    filter_method=0,
    interlace_method=0):

  ihdr = b""
  ihdr += width
  ihdr += height
  ihdr += bytes([
      bit_depth, colour_type, compression_method, filter_method,
      interlace_method
  ])

  return ihdr


def read_rgb_subpixel(rgb_data, width, x, y, subpixel):
  return rgb_data[3 * ((width * y) + x) + subpixel]


def apply_png_filters(rgb_data, width, height):
  filtered = []
  for y in range(height):
    filtered.append(0)
    for x in range(width):
      filtered += [
          read_rgb_subpixel(rgb_data, width, x, y, 0),
          read_rgb_subpixel(rgb_data, width, x, y, 1),
          read_rgb_subpixel(rgb_data, width, x, y, 2)
      ]
  return bytes(filtered)


if __name__ == "__main__":
  INPUT_WIDTH = 500
  INPUT_HEIGHT = 619
  # convert og.png og.rgb
  input_rgb_data = open("og.rgb", "rb").read()

  ihdr = encode_png_ihdr(INPUT_WIDTH, INPUT_HEIGHT)

  filtered = apply_png_filters(input_rgb_data, INPUT_WIDTH, INPUT_HEIGHT)

  idat = zstandard.compress(filtered, level=19)

  with open("../chunky.meme", "wb") as f:
    f.write(PNG_SIGNATURE)
    write_png_chunk(f, b"IHDR", ihdr)
    write_png_chunk(f, b"IDAT", idat)
    write_png_chunk(f, b"IEND", b"")
