#!/usr/bin/python3
""" taks """
from sys import argv
import MySQLdb


if __name__ == "__main__":
	mydb = MySQLdb.connect(host= "localhost",user="argv[0]",passwd="argv[1]",db="hbtn_0e_0_usa")
	s = mydb.cursor()
	s.execute("select id,states from states order by id asc")
	for i in s:
		print(i)
	s.close()
        mydb.close()
