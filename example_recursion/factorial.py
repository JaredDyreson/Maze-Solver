#!/usr/bin/env python3.5

def factorial(number : int):
    if(number == 1): return number
    else:
      return (number*factorial(number-1))

for x in range(1, 10):
  print("{} -> {}".format(x, factorial(x)))

