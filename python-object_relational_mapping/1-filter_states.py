#!/usr/bin/python3
""" 1st     """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    cnt = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    s = cnt.cursor()
    a = "SELECT id,name FROM states WHERE name LIKE BINARY'N%' ORDER BY id ASC"
    s.execute(a)
    res = s.fetchall()
    for i in res:
        print(i)
    s.close()
    cnt.close()
