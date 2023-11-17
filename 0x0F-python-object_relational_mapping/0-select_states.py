#!/usr/bin/python3
"""Get all states module"""

import MySQLdb

dbc = MySQLdb.connect(host="localhost", port=3306,
                      user="sam", password="sam", db="hbtn_0e_0_usa")

cur = dbc.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
if __name__ == "__main__":
    for row in rows:
        print(row)
    cur.close()
    dbc.close()
