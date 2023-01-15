#!/usr/bin/python3
"""class-checking function."""


def inherits_from(obj, a_class):
    """Checks is subclass or not """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
