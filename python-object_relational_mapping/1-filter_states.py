#!/usr/bin/python3
""" 1st     """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    cnt = MySQLdb.connect(user=argv[0],passwd=argv[1],db=argv[2])
    s = cnt.cursor()
    s.execute("SELECT id,name FROM states WHERE name LIKE = N% ORDER BY id ASC")
    for i in s:
        print(i)
    s.close()
    cnt.close()
