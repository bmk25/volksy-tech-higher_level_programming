#!/usr/bin/python
def upper(string):

    new_string =''

    for i in range(len(string)):

        if(string[i] >= 'a' and string[i] <= 'z'):

            new_string = new_string + chr((ord(string[i]) - 32))

        else:

            new_string = new_string + string[i]

            print(new_string)
