#!/usr/bin/python3
"""This module define a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from relationship_state import Base, State
    from relationship_city import City

    args = sys.argv[1:]
    username, password, database = tuple(args)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                    password,
                                                    database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='California')
    state.cities = [City(name='San Francisco')]
    session.add(state)
    session.commit()
