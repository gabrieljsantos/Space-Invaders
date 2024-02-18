from Setup_tela import *
from Setup_Game import *
import random

objects = []
def alien_generator():
    generator = True
    #while generator == True:
    for i in range(11):
        objects.append(['alien b', 0, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), (32+13*i), 26])
    for i in range(10):
        objects.append(['alien a', 0, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), (32+13*i), 39])
    for i in range(8):
        objects.append(['alien a', 0, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), (32+13*i), 52])
    for i in range(11):
        objects.append(['alien c', 0, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), (32+13*i), 65])
    for i in range(8):
        objects.append(['alien c', 0, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), (32+13*i), 78])
