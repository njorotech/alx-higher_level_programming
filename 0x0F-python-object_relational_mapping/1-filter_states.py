#!/usr/bin/python3
"""Lists all states with a name starting with N"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    databaseName = argv[3]

    dbc = MySQLdb.connect(host="localhost", port=3306,
                          user=user, passwd=password, db=databaseName)

    cur = dbc.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dbc.close()
