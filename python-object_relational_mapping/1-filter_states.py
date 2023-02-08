#!/usr/bin/python3
""" 1st     """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    cnt = MySQLdb.connect(user=argv[1],passwd=argv[2],db=argv[3])
    s = cnt.cursor()
    s.execute("SELECT id,name FROM states WHERE name LIKE = N% ORDER BY id ASC")
    for i in s:
        print(i)
    s.close()
    cnt.close()
