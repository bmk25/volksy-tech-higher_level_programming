#!/usr/bin/python3
def safe_print_list(my_list=[], x = 0):
        try:
            if x <= (len(my_list)-1):
                for i in range(x):
                    print(my_list[i],end="")
                print()
                return x
            else:
                return x
        except IndexError:
            print(x)
