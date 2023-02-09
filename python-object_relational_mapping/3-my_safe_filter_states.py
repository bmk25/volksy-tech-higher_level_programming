#!/usr/bin/python3
"""
safe sql injection
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    txt1 = argv[4]
    sql = "SELECT * FROM states WHERE NAME BINARY LIKE @0 ORDER BY id ASC"
    c.execute(sql,txt1)
    db.close()
