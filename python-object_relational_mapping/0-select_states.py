#!/usr/bin/python3
"""
0 task 
"""
if __name__ == "__main__":
        from sys import argv
	import MySQLdb
	mydb = MySQLdb.connect(host= "localhost",user="argv[0]",passwd="argv[1]",db="hbtn_0e_0_usa")
	s = mydb.cursor()
	s.execute("select id,states from states order asc")
	for i in s:
		print(i)
	s.close()
        mydb.close()
