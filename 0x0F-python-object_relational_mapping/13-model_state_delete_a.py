#!/usr/bin/python3
"""This module define a script that deletes all State
objects with a name containing the letter a from the database
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    args = argv[1:]
    username, password, database = tuple(args)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                    password,
                                                    database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        if 'a' in state.name:
            session.delete(state)
    session.commit()
