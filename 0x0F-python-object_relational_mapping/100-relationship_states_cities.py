#!/usr/bin/python3
"""This module define a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from relationship_state import State
    from relationship_city import Base, City

    args = sys.argv[1:]
    username, password, database = tuple(args)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                    password,
                                                    database)
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name='San Francisco', state=State(name='California')))
    session.commit()
