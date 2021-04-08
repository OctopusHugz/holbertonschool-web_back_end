#!/usr/bin/env python3
""" This module implements an Auth class """
from app import AUTH
from db import DB
from sqlalchemy.exc import NoResultFound
from typing import TypeVar, Union
from uuid import uuid4
import bcrypt


def _hash_password(password: str) -> str:
    """ Hashes a plaintext password using bcrypt.hashpw """
    return bcrypt.hashpw(password.encode(),
                         bcrypt.gensalt()).decode('utf-8')


def _generate_uuid() -> str:
    """ Returns a string of a new uuid """
    return str(uuid4())


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
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Locates user by email, and checks password with bcrypt.checkpw"""
        try:
            found_user = self._db.find_user_by(email=email)
            if found_user is not None:
                return bcrypt.checkpw(password.encode(),
                                      found_user.hashed_password.encode())
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Takes an email and returns a session ID """
        try:
            found_user = self._db.find_user_by(email=email)
            if found_user is not None:
                session_id = _generate_uuid()
                user_data = {"session_id": session_id}
                self._db.update_user(found_user.id, **user_data)
                return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """ Finds a user based on a session_id and returns it """
        # This method needs more clarity on the return value type
        if session_id is None:
            return None
        try:
            found_user = self._db.find_user_by(session_id=session_id)
            return found_user
        except NoResultFound:
            return None
