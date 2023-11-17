#!/usr/bin/python3
"""Lists all cities of a given state"""

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

    querry = """SELECT cities.name
        FROM cities JOIN states ON cities.state_id = states.id
        WHERE states.name = %s ORDER BY cities.id ASC"""
    cur.execute(querry, (stateName,))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[0])
    print(', '.join(cities))
    cur.close()
    dbc.close()
