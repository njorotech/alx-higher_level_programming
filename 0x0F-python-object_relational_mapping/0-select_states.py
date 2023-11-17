#!/usr/bin/python3
"""Get all states module"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    databaseName = argv[3]

    dbc = MySQLdb.connect(host="localhost", port=3306,
                          user=user, password=password, db=databaseName)

    cur = dbc.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dbc.close()
