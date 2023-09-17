#!/usr/bin/python3
"""This module define a script that that adds the
State object “Louisiana” to the database
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

    new_state = State(name='Louisiana')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(new_state)
    session.commit()
