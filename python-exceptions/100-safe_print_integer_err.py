#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if "{:d}".format(value) :
            print(value)
            return True
    except:
        print("Exception: Unknown format code 'd' for object of type 'str'")
        return False
