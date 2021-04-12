#!/usr/bin/env python3
""" This module implements an Auth class """
from user import User
from db import DB
from sqlalchemy.exc import NoResultFound
from typing import TypeVar, Union
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Hashes a plaintext password and returns salted hash """
    from bcrypt import gensalt, hashpw
    if password is None or not isinstance(password, str):
        return None
    return hashpw(password.encode(), gensalt())


def _generate_uuid() -> str:
    """ Returns a string of a new uuid """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Instantiate an Auth instance """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user in the DB """
        try:
            found_user = self._db.find_user_by(email=email)
            if found_user is not None:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Locates user by email, and checks password"""
        from bcrypt import checkpw
        try:
            found_user = self._db.find_user_by(email=email)
            if found_user is not None:
                return checkpw(password, found_user.hashed_password)
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

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ Finds a user based on a session_id and returns it """
        # This method needs more clarity on the return value type
        if session_id is None:
            return None
        try:
            found_user = self._db.find_user_by(session_id=session_id)
            return found_user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """ Updates the user's (based on user_id) session ID to None """
        try:
            found_user = self._db.find_user_by(id=user_id)
            user_data = {"session_id": None}
            self._db.update_user(found_user.id, **user_data)
            return None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Generates a reset_token and updates it for user found by email """
        try:
            found_user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(found_user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Updates a user password to provided password using reset token """
        try:
            found_user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            user_data = {"hashed_password": hashed_password,
                         "reset_token": None}
            self._db.update_user(found_user.id, **user_data)
            return None
        except NoResultFound:
            raise ValueError
