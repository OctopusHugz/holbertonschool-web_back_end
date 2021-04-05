#!/usr/bin/env python3
""" This module implements the SessionDBAuth class """
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Instance of the SessionDBAuth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id=None):
        """ Creates a session for a user_id """

    def user_id_for_session_id(self, session_id=None):
        """ Returns a user_id from a session_id """

    def destroy_session(self, request=None):
        """ Deletes the user session/logs the user out """
