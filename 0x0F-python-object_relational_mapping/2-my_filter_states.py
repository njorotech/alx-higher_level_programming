#!/usr/bin/python3
"""Filter states by user input"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    databaseName = argv[3]
    stateName = argv[4]

    dbc = MySQLdb.connect(host="localhost", port=3306,
                          user=user, passwd=password, db=databaseName)

    cur = dbc.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(stateName))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dbc.close()
