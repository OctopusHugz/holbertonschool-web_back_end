#!/usr/bin/env python3
""" This module creates a DB class """
from typing import TypeVar
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base, User


class DB:

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=True)
        # self._engine = create_engine(
            "sqlite:///a.db", connect_args={"check_same_thread": False})

        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> TypeVar("User"):
        """ This method adds a user to the DB """
        new_user = User()
        new_user.email = email
        new_user.hashed_password = hashed_password
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> TypeVar("User"):
        """ Returns first row found in users table with args from kwargs """
        found_user = self._session.query(User).filter_by(**kwargs).one()
        # change .one() back to .first() ?
        # if found_user is None:
        #     raise NoResultFound
        return found_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Updates a user row with args from kwargs in the DB """
        found_user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in found_user.__dict__:
                raise ValueError
            setattr(found_user, key, value)
        self._session.commit()
        return None
