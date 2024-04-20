with open('../chal', 'rb') as file:
  with open('solve.png', 'wb') as out:
    while mbytes := file.read(4):
      out.write(bytes(reversed(mbytes)))
