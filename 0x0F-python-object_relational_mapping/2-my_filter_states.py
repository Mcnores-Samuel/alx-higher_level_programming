#!/usr/bin/python3
"""This module provides a script that  takes in an argument
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.

Usage:
    ./2-my_filter_states.py <mysql username> <mysql password>
            <database name> <state name searched>
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    args = sys.argv[1:]
    try:
        username, password, database, state = tuple(args)
        db = MySQLdb.connect(
            user=username,
            password=password,
            database=database
        )
        db_cursor = db.cursor()
        db_cursor.execute(
            "SELECT * FROM states WHERE name = '{}'\
                  ORDER BY states.id ASC".format(state))
        states = db_cursor.fetchall()
        for s in states:
            print(s)
    except ValueError:
        pass
