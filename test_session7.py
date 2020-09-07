import pytest , os , inspect , re , random,session7
from decimal import Decimal
import math
import random
from functools import partial
from functools import reduce

def test_add_iterables():
    a=[1,2,3,4,5,6]
    b=[10,9,4,13,11,17]
    d = [(x+y) for x in a if x%2==0 for y in b if y%2!=0 ]
    assert d == [11, 15, 13, 19, 13, 17, 15, 21, 15, 19, 17, 23]


def test_strip_vowels():
    l="tsai"
    k=[i for i in l if i not in ('a','e','i','o','u') ]
    s="".join(i for i in k)
    assert s == 'ts'


def test_Relu_function():
    a=[-1,2,3,-4,5]
    k=[i if i>0 else 0 for i in a]
    assert k == [0, 2, 3, 0, 5]


def test_sigmoid_function():
    a=[-2,-3,2,3,4]
    k=[1 if i>=1 else 0 for i in a]
    assert k == [0, 0, 1, 1, 1]


def test_shift_characters():
    a="tsai"
    k=[chr(ord(i)+5) for i in a]
    p="".join(i for i in k)
    assert p == 'yxfn'


def generate_random_number_plates():
    z=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a=["KA"+str(random.randint(11,98))+str(random.choice(z))+str(random.choice(z))+str(random.randint(1001,9998)) for i in range(15)]
    assert type(a) is list


def test_number_plate_partial():
    f=partial(session7.numberplate,b=1011)
    k=f('DL')
    assert type(k) is list


def test_reduce_add_even_number_():
    s=reduce(lambda a,b:(a+b),session7.generate_even_number_list())
    assert s == 30

