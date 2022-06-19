#!usr/bin/python3
"""show states in database"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
	db = MySQLdb.connect(
		host = "localhost",
		port =3306,
		user=argv[1],
		passwd=argv[2],
		db=argv[3],
		charset="utf8"
	)
	c = db.cursor()
	c.excute("SELECT * FROM states ORDER BY id ASC")
	rows = c.fetchall()
	for r in rows:
		print(r)
		c.close()
		db.close()
