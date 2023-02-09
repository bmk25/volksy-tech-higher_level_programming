#!/usr/bin/python3
""" 1st     """
from sys import argv
import MySQLdb


if __name__ ==__main__:
    mydb = MySQLdb.connect(user= argv[1],passwd=argv[2],db=argv[3])
    s = mydb.cursor()
    a = s.execute (f"SELECT * FROM states WHERE name = {argv[4]}")
    for i in a:
        print(i)
    mydb.close()`
