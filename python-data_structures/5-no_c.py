#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            # print("{}".format(""), end="")
            str = str + ""
        else:
            # print("{}".format(i), end="")
            str = str + ("{}".format(i))
    return str
