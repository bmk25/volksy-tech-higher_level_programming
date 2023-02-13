#!/usr/bin/python3
''' hello'''
def text_indentation(text):
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for i in text:
        if i == "." or i== "?" or i== ":":
            print(i)
            print("\n")
            continue
        print(i,end="")
