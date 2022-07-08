#!/usr/bin/python3
"""
    safe from MySQL injections
"""
import MySQLdb
from sys import argv

def safe():
    """Host Connect"""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    """let them safe"""
    command = """SELECT *
                 FROM states
                 WHERE BINARY states.name = %s
                 ORDER BY states.id ASC"""
    numrows = c.execute(command, (argv[4],))
    states = c.fetchall()
    for idstate in states:
        print(idstate)

"""execute"""
if __name__ == "__main__":
    safe()
