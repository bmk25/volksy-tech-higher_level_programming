#!/usr/bin/python3
"""
safe sql injection
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306 )
    c = db.cursor()
    sql = "select cities.state_id,cities.name,states.name\
           from cities inner join states on cities.state_id = states.id\
           order by cities.state_id"
    c.execute(sql)
    for i in c.fetchall():
        print(i)
    c.close()
    db.close()
