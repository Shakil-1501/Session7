import pytest , os , inspect , re , random,session7
from decimal import Decimal
import math
import random
from functools import partial

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
    a=["KA"+str(random.randint(11,98))+str(random.choice(z))+str(random.choice(z))+str(random.randint(1001,9998)) for i in range(15)]
    assert a == ['KA75QX3380',
    'KA12VG3345',
    'KA94BO7337',
    'KA92NM3444',
    'KA11SG2740',
    'KA21JV8053',
    'KA92RQ2666',
    'KA94SU8245',
    'KA44UB8036',
    'KA15GV4698',
    'KA66DU5043',
    'KA56BY1202',
    'KA82KC3901',
    'KA92US2708',
    'KA47AC7116']


def test_number_plate_partial():
    f=partial(session7.numberplate,b=1011)
    
    assert f('DL') == ['DL58RB1011', 'DL58LT1011', 'DL91SL1011', 'DL77AE1011', 'DL90FA1011', 'DL66EV1011', 'DL57PB1011', 'DL63GR1011', 'DL13YR1011', 'DL44CA1011', 'DL77HG1011', 'DL60VJ1011', 'DL58JK1011', 'DL45LZ1011', 'DL19FF1011']


