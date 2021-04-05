#!/usr/bin/env python3
""" This module implements the SessionAuth class """
from flask.globals import session
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Instance of the SessionAuth class, which inherits from Auth """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session ID for a user ID """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a User ID based on a Session ID """
        if session_id is None or not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a User instance based on a cookie value """
        session_id = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Deletes the user session/logs the user out """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        elif self.user_id_for_session_id(session_id) is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
