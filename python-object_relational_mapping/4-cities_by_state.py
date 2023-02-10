#!/usr/bin/python3
"""
safe sql injection
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306 )
    c = db.cursor()
    sql = "select id,name from cities order by id"
    c.execute(sql)
    for i in c.fetchall():
        print(i)
    c.close()
    db.close()
