#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

if __name__ == '__main__':
    # Standard Library imports
    import sys

    # related third party imports
    import MySQLdb as sql

    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    conn = sql.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=passwd,
            db=database)

    cur = conn.cursor()

    cur.execute("SELECT * FROM cities ORDER BY cities.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
