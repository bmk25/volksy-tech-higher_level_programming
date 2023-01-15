#!/usr/bin/python3
"""class-checking function."""


def is_kind_of_class(obj, a_class):
    """ is instance """
    if isinstance(obj, a_class):
        return True
    return False
