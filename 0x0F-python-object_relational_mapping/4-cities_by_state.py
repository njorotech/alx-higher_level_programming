#!/usr/bin/python3
"""Lists all cities from database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    databaseName = argv[3]

    dbc = MySQLdb.connect(host="localhost", port=3306,
                          user=user, passwd=password, db=databaseName)

    cur = dbc.cursor()

    querry = """SELECT cities.id, cities.name, states.name
        FROM cities JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC"""
    cur.execute(querry)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dbc.close()
