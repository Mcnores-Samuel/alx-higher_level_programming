#!/usr/bin/python3
"""This module define a script that  lists all State objects,
and corresponding City objects, contained in the database
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
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
