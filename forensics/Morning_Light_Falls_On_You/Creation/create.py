with open('og.png', 'rb') as file:
  with open('../chal', 'wb') as out:
    while mbytes := file.read(4):
      out.write(bytes(reversed(mbytes)))
