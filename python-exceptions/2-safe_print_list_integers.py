#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for i in range(x):
        try:
            if "{:d}".format(my_list[i]):
                print("{:d}".format(my_list[i]), end="")
                y = y + 1
        except (TypeError, ValueError):
            continue
        except (IndexError):
            raise
    print()
    return(y)
