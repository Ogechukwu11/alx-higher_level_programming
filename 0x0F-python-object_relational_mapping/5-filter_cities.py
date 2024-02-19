#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
                INNER JOIN states ON states.id=cities.state_id \
                WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
