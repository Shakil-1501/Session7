import pytest , os , inspect , re , random
from decimal import Decimal
import math
import cmath


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







