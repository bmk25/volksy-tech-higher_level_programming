#!/usr/bin/python3
#/usr/bin/python3
"""
safe sql injection
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE NAME = %(name)s ORDER BY id ASC",{'name' :argv[4]})
    row = c.fetchall()
    for i in row:
        print(i)
    c.close(i)
    db.close()
