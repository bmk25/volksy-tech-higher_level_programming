#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside reslt :{:d}".format(a/b))
    except ZeroDivisionError:
        print("Inside reslt :{}".format(None))
        return None 
    finally:
        try:
            return a / b
        except ZeroDivisionError:
            return None
