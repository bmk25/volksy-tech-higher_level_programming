#!/usr/bin/python3
'''Hello world '''


class Square:
    """helo"""
    def __init__(self, size=0):
        try:
            if size >= 0:
                self.__size = size
        except TypeError:
                print("size must be an integer")
        except ValueError:
                print("size must be >= 0")
