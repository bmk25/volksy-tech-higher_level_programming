#!/usr/bin/python3
import MySQLdb
""" 1st     """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    cnt = MySQLdb.connect(user=argv[0],passwd=argv[1],db=argv[2])
    cnt.execute("SELECT id,name FROM states WHERE name LIKE = N% ORDER BY id ASC")
    for i in cnt:
        print(i)
    cnt.close()
