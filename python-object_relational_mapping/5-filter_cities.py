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
           from cities inner join states on cities.state_id = cities.id\
           where cities.state_id = (select id from states where name = '%(name)s')",\
           {'name': argv[4]}
    c.execute(sql)
    row = c.fetchall()
    [print(i, end=",") for i in row]
    c.close()
    db.close()
