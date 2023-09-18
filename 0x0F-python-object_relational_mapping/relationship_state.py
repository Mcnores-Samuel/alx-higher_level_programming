#!/usr/bin/python3
"""This module provides or defines a State class
representing a table in the database
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """definition of state class representing a table in the database"""
    __tablename__ = 'states'
    id = Column('id', Integer(), unique=True, primary_key=True,
                autoincrement=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship('Cities', backref='state',
                          cascade='all, delete')
