#!/usr/bin/python3
""" append the new file"""


def append_write(filename="", text=""):
    """ append new text and find the no of characters"""

    with open(filename, "a+", encoding="utf=8") as f:
        f.write(text)
        return (len(text))
