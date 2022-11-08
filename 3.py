from math import *

x, y = int(input()), int(input())

def func(arg_x, arg_y):
    print(sin(arg_y + 0.5) + arg_x - 1)
    print(arg_y |+ cos(arg_x - 2))

func(x, y)