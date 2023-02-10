#!/usr/bin/python3
"""
safe sql injection
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306 )
    c = db.cursor()
    sql = "select cities.name\
           from cities \
           where state_id = (select id\
           from states where states.name = %(name)s)",{'name': argv[4]}
    c.execute(sql)
    row = c.fetchall()
    [print(i[0], end=",") for i in row]
    c.close()
    db.close()
