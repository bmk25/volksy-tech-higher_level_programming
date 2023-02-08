#!/usr/bin/python3
''' task 1  '''
from sys import argv
import MySQLdb

if __name__ == '__main__':
	mydb = MySQLdb.connect(host= "argv[0]",user="argv[1]",passwd="argv[2]",database="hbtn_0e_0_usa")
	s = mydb.cursor()
	s.execute("select * from states")
	for i in s:
		print(i)
        s.close()
        mydb.close() 
