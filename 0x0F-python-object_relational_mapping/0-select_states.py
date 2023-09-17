#!/usr/bin/python3
"""This module provides a script for reading data from mysql database

Lists all states from the database hbtn_0e_0_usa

Usage:
    ./0-select_states.py <mysql username> <mysql password> <database name>
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    args = sys.argv

    try:
        database = MySQLdb.connect(
            host='localhost', port=3306,
            user=args[1], password=args[2],
            database=args[3]
        )

        db_cursor = database.cursor()
        db_cursor.execute("""
                          SELECT * FROM states ORDER BY states.id ASC
                          """)
        states = db_cursor.fetchall()
        for state in states:
            print(state)
    except IndexError:
        pass
