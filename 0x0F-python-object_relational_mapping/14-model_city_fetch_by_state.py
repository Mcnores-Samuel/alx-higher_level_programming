#!/usr/bin/python3
"""This module define a script that  lists all states and there cities"""
if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import Cities

    args = sys.argv[1:]
    username, password, database = tuple(args)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                    password,
                                                    database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, Cities).\
        filter(State.id == Cities.state_id)\
        .order_by(Cities.id).all()

    for state, city in query:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
