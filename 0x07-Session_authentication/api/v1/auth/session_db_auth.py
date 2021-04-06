#!/usr/bin/env python3
""" This module implements the SessionDBAuth class """
from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Instance of the SessionDBAuth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id=None):
        """ Creates a session for a user_id """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        new_user_session = UserSession(session_id=session_id, user_id=user_id)
        self.user_id_by_session_id[session_id] = new_user_session
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns a user_id from a session_id """
        user_session = self.user_id_by_session_id.get(session_id)
        if user_session is not None:
            return user_session.user_id
        else:
            return None

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
