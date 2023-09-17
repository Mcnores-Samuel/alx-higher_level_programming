#!/usr/bin/python3
"""This module provides a script that lists all State objects
from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    args = sys.argv[1:]
    username, password, database = tuple(args)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                    password,
                                                    database)
    )

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).all()
    for state in query:
        print('{}: {}'.format(state.id, state.name))
