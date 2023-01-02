#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n1 = number % -10
    print("Last digit of", number, "is", n1, "and is less than 6 and not 0")
elif number > 0:
    n2 = number % 10
    if n2 > 5:
        print("Last digit of", number, "is", n2, "and is greater than 5")
    else:
        print(
              "Last digit on", number,
              "is", n2,
              "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is 0 and is 0")
