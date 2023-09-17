#!/usr/bin/python3
"""This module provides a script that takes in the name of
a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa

Usage:
    ./4-cities_by_state.py <mysql username> <mysql password> <database name>
        <state name>
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
        db_cursor.execute("SELECT `cities`.`name`\
                          FROM cities INNER JOIN `states` as `state` \
                          ON `state`.`id` = `cities`.`state_id` \
                          WHERE `state`.`name` = %s\
                          ORDER BY `cities`.`id`", (state,))
        cities = db_cursor.fetchall()
        if cities:
            for city in cities:
                print(city[0], end='')
                if city != cities[-1]:
                    print(', ', end='')
                else:
                    print()
        else:
            print()
    except ValueError:
        pass
