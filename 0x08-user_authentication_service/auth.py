#!/usr/bin/env python3
""" This module implements an Auth class """
from user import User
from db import DB
from sqlalchemy.exc import NoResultFound
from typing import TypeVar
import bcrypt


def _hash_password(password: str) -> str:
    """ Hashes a plaintext password using bcrypt.hashpw """
    return bcrypt.hashpw(password.encode(),
                         bcrypt.gensalt()).decode('utf-8')


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar("User"):
        """ Registers a user in the DB """
        try:
            found_user = self._db.find_user_by(email=email)
            if found_user is not None:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            self._db.add_user(email, hashed_password)
