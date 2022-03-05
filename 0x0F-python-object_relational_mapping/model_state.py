#!/usr/bin/python3
""" module that contains the class definition of a State and an instance
"""

# related third party imports

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
