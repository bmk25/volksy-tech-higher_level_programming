#/usr/bin/python3
"""
safe sql injection
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = connect(user=argv[1], passwd=argv[2], db=argv[4])
    c = db.cursor()
    txt1 = f"{argv[4]}"
    sql = "SELECT * FROM states WHERE NAME BINARY LIKE @0"
    c.execute(sql,txt1)
    db.close()

