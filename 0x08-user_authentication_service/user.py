#!/usr/bin/env python3
""" This module creates a User class """
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import INTEGER, VARCHAR

Base = declarative_base()


class User(Base):
    """ Instance of User class """
    __tablename__ = 'users'

    id = Column(INTEGER, primary_key=True)
    email = Column(VARCHAR(250), nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250), nullable=True)
    reset_token = Column(VARCHAR(250), nullable=True)
