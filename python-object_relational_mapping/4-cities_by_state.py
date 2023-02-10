#!/usr/bin/python3
"""
this is combine
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("select cities.id,cities.name,states.name\
               from cities inner join states on cities.state_id = states.id\
               order by cities.id")
    [print(i) for i in c.fetchall()]
    c.close()
    db.close()
