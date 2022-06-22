# write function named is _perfect_square that accept a number and return True if it's a perfect square and False if it's not.

import math

def _perfect_square(num):
    if num>=0:
        square = int(math.sqrt(num))
        if (square*square == num):
            print(f"{num}  is perfect square")
        else:
            print(f"{num} is not perfect square")

_perfect_square(24)