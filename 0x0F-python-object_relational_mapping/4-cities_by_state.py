#!/usr/bin/python3
"""This module provides a script for listing all
cities from the database hbtn_0e_4_usa

Usage:
    ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    args = sys.argv[1:]
    try:
        username, password, database = tuple(args)
        db = MySQLdb.connect(
            user=username,
            password=password,
            database=database
        )
        db_cursor = db.cursor()
        db_cursor.execute("SELECT\
        `cities`.`id`, `cities`.`name`, `state`.`name`\
                          FROM cities INNER JOIN `states` as `state` \
                          ON `state`.`id` = `cities`.`state_id` \
                          ORDER BY `cities`.`id`")
        cities = db_cursor.fetchall()
        for city in cities:
            print(city)
    except ValueError:
        pass
