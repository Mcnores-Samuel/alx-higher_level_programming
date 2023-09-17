#!/usr/bin/python3
"""This module define a script that prints the State object with
the name passed as argument from the database
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    args = argv[1:]
    username, password, database, state_name = tuple(args)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                    password,
                                                    database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name == state_name).first()
    if query:
        print(query.id)
    else:
        print('Not found')
