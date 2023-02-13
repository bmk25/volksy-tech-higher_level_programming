#!/usr/bin/python3
""" first name and last name """


def say_my_name(first_name, last_name=""):
    """ two must be the strings"""
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    return (first_name + last_name)
