#!/usr/bin/python3
''' hello'''

def print_square(size):
    '''about the square'''


    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0 or isinstance(size, float):
        raise TypeError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
