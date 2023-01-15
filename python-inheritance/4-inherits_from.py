#!/usr/bin/python3
"""class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check is an instance of a obbject 
    ir nto
    """
    if isinstance(obj, a_class):
        return True
    return False
