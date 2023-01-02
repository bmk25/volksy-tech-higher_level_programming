#!/usr/bin/python3
for i in reversed(range(65, 91)):
    print("{}".format(chr(i) if i % 2 != 0 else chr(i+32)), end="")
