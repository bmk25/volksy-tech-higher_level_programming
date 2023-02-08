#!/usr/bin/python3
''' o task '''
if __name__ == __main__:
	from sys import argv
	import MySQLdb
	mydb = MySQLdb.connect(host= "argv[0]",user="argv[1]",passwd="argv[2]",database="hbtn_0e_0_usa")
	s = mydb.cursor()
	s.execute("select * from states")
	for i in s:
		print(i)
        mydb.close() 
