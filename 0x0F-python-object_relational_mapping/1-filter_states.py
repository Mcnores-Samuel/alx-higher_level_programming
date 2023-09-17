#!/usr/bin/python3
"""This module provides a script for  listing all states with
a name starting with N (upper N) from the database hbtn_0e_0_usa

Usage:
    Takes 3 arguments: mysql username, mysql password and database name
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv[1:]
    username, password, database = tuple(args)
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        password=password,
        database=database
    )

    db_cursor = db.cursor()
    db_cursor.execute("""SELECT * FROM states WHERE name LIKE 'N%'
            ORDER BY states.id ASC
    """)

    states = db_cursor.fetchall()
    for state in states:
        print(state)
