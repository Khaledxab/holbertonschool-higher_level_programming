#!/usr/bin/python3
"""
    list cities from Db
"""
import MySQLdb
from sys import argv


def exec():
    """Connect"""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    command = """SELECT cities.id, cities.name, states.name
                 FROM cities, states
                 WHERE cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    numrows = c.execute(command)
    states = c.fetchall()
    for idstate in states:
        print(idstate)


"""execute"""
if __name__ == "__main__":
    exec()
