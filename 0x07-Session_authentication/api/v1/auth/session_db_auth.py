#!/usr/bin/env python3
""" This module implements the SessionDBAuth class """
from models.base import DATA
from typing import Union
from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Instance of the SessionDBAuth class"""

    def create_session(self, user_id=None) -> Union[str, None]:
        """ Creates a session for a user_id """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        new_user_session = UserSession(session_id=session_id, user_id=user_id)
        new_user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None) -> Union[str, None]:
        """ Returns a user_id from a session_id """
        UserSession.load_from_file()
        user_session_list = UserSession.search({"session_id": session_id})
        if len(user_session_list) > 0:
            for user_session in user_session_list:
                if user_session.session_id == session_id:
                    return user_session.user_id
        return None

    def destroy_session(self, request=None) -> bool:
        """ Deletes the user session/logs the user out """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        destroy_list = UserSession.search({"session_id": session_id})
        if len(destroy_list) > 0:
            for user_session in destroy_list:
                if user_session.session_id == session_id:
                    user_session.remove()
        return True
