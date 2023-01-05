#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i == ('c' or 'C'):
            print("{}".format(""),end="")
        else:
            print("{}".format(i),end="")
    return my_string
