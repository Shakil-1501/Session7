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


def generate_every_thirdelement_list():
    k=[]
    s=[1,2,3,4,5,6,7,8,9,10]
    for i in range(0,len(s),3):
        k.append(s[i])
    return k


def generate_biggest_character_string():
    k=reduce(lambda a,b :a if a>b else b,[x for x in 'tsai'])
    assert k == 't'


def check_word_exists():
    with open('list.txt') as file:
    contents=file.read()
    search=" hello motherfucker how are you dickhead asshole.Terrorism is a big national issue which is using the human mind to get complete victory. Terrorism is terrifying the mind of the human being to make them weak so that they can rule the nation again. It needs to be solved on international level. We all should think about terrorism together to finish it from the root. We should make a strong policy to completely destroy its kingdom as well as removing the striking terror from the human minds. Terrorism uses violent ways to achieve the purpose and get positive result.\
                Terrorism is the act of violence performed by the group of people called terrorist. They become very common people and somehow they lost their control over the mind because of some unfair natural disasters or unfair activities with them by others which make them unable to fulfil desires in normal and accepted ways. Slowly they are taken under the confidence of some bad people in the society where they are promised to get fulfilled all the desires. They get together and form a group of terrorists to fight with their own nation, society and community. Terrorism has affected all the youths of the country, their growth and development."
    k=search.split()
    l=['word found is {}'.format(z)  for z in k if z in contents ]
     assert type(l) is list
