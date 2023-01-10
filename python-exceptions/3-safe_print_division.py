#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside reslt :",a/b)
    except ZeroDivisionError:
        print("Inside reslt : None")
        return None 
    finally:
        try:
            return a / b
        except ZeroDivisionError:
            return None
