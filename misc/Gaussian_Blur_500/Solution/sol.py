import cv2 as cv
import numpy as np

original = cv.imread('../chal.png')

recovered = np.zeros(original.shape, dtype=np.uint8)
recovered.fill(255)

equ = lambda ret: 30 + ret * 10


def paint(x, y, dark, im):
  if dark:
    im[equ(x):equ(x) + 10, equ(y):equ(y) + 10] = [0, 0, 0]
  else:
    im[equ(x):equ(x) + 10, equ(y):equ(y) + 10] = [255, 255, 255]


def difference(i, j, im):
  blurred = cv.GaussianBlur(im, (45, 45), 0)
  diff = blurred[equ(i):equ(i) + 10, equ(j):equ(j) + 10,
                 0] - original[equ(i):equ(i) + 10,
                               equ(j):equ(j) + 10, 0]
  diff[diff > 128] = 255 - diff[diff > 128]
  return diff.sum()


for i in range(0, 45):
  for j in range(0, 45):
    min_diff = difference(i, j, recovered)
    is_paint = False
    bruteforce = recovered.copy()

    for mask in range(0, 2**7):
      for ii, jj, c in zip([0, 0, 0, 1, 1, 1, 2], [0, 1, 2, -1, 0, 1, 0],
                           range(7)):
        ii += i
        jj += j
        if ii < 0 or ii >= 45 or jj < 0 or jj >= 45:
          continue

        if mask & (1 << (c)):
          paint(ii, jj, True, bruteforce)
        else:
          paint(ii, jj, False, bruteforce)

      new_diff = difference(i, j, bruteforce)
      if new_diff < min_diff:
        min_diff = new_diff
        is_paint = mask & 1

    paint(i, j, is_paint, recovered)
    cv.imshow('recovered', recovered)
    cv.waitKey(10)

cv.imwrite("solve.png", recovered)
