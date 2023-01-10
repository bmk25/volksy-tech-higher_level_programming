#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if "{:d}".format(value) :
            print(value)
            return True
    except Exception as e:
        print("Exception: " + str(e), file=sys.stderr)
        return False
