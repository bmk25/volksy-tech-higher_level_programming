#!/usr/bin/python3
""" hello"""


def add_integer(a, b=98):
    """ hello"""

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
