#!/usr/bin/python3
"""
safe sql injection
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM cities\
                INNER JOIN states\
                   ON cities.state_id = states.id \
                ORDER BY cities.id")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == argv[4]]))
