#!/usr/bin/python3
"""This module provides a class for connecting to a table
in the database
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, ForeignKey

Base = declarative_base()


class City(Base):
    """Definition of the Cities class representing a cities table in the
    database

    Table Columns:
        id: a unique id Integer for positioning an object in the database
        name: city name
        state_id: an id from which the city belongs to.
    """
    __tablename__ = 'cities'
    id = Column('id', Integer(), unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer(), ForeignKey('states.id'),
                      nullable=False)
