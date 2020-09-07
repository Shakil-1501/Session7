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


def numberplate(a,b):
    z=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s=[a+str(random.randint(11,98))+str(random.choice(z))+str(random.choice(z))+str(b) for i in range(15)]
    return s


def generate_even_number_list():
    k=[]
    s=[1,2,3,4,5,6,7,8,9,10]
    for i in s:
        if i%2==0:
            k.append(i)
    return k