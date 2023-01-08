#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ls1 = list(tuple_a)
    ls2 = list(tuple_b)
    ls3 = []
    for i in range(2):
        ls1.append(0)
        ls2.append(0)
        ls3.append(ls1[i] + ls2[i])
    tup1 = tuple(ls3)
    return tup1
