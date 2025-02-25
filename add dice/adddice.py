import random

def dice(n):
  p = 0
  total = 0
  while p < n:
    total += random.randint(1,6)
    p += 1
  print total
dice(3)

