from typing import List
import time
import sys
import weakref
import random
from math import tan, pi


numbers = range(10000)

# function that filters vowels
def filterFibnocci(number):
    a=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

    if(number in a):
        return True
    else:
        return False


