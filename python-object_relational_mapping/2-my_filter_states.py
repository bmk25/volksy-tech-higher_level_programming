#!/usr/bin/python3
''' match the naem argument '''


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states
                WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
    for i in c:
        print(i)
    db.close()
