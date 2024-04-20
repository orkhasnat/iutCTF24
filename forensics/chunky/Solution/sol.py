import zstandard
import zlib

img_data = open('../chunky.meme', 'rb').read()
signature, img_data = img_data[:8], img_data[8:]
img_data, iend = img_data[:-12], img_data[-12:]
ihdr, idat = img_data[:25], img_data[25:]

ihdr = ihdr[:18] + b'\x00' + ihdr[18 + 1:-4]
ihdr += zlib.crc32(ihdr[4:]).to_bytes(4, 'big')

idat = idat[8:-4]
new_idat = zlib.compress(zstandard.decompress(idat), level=9)

new_idat = len(new_idat).to_bytes(4, "big") 
            + b'IDAT' 
            + new_idat 
            + zlib.crc32(b'IDAT' + new_idat).to_bytes(4, 'big')
            
open('solve.png', 'wb').write(signature + ihdr + new_idat + iend)
