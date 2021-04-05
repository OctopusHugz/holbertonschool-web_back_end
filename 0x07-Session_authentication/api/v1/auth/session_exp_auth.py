#!/usr/bin/env python3
""" This module implements the SessionExpAuth class """
from flask.globals import session
from models.user import User
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """Instance of the SessionExpAuth class, which inherits from SessionAuth"""
    user_id_by_session_id = {}

    def __init__(self):
        """ Instantiate an instance of SessionExpAuth class """
        sd = os.getenv("SESSION_DURATION")
        if sd:
            self.session_duration = int(sd)
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Creates a session for a user_id """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dict = {}
        session_dict["user_id"] = user_id
        session_dict["created_at"] = datetime.now()
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Returns a user_id from a session_id """
        if session_id is None or self.user_id_by_session_id.get(
                session_id) is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if self.session_duration <= 0:
            return session_dict.get("user_id")
        created_at = session_dict.get("created_at")
        if created_at is None:
            return None
        expiration_date = created_at + timedelta(
            seconds=self.session_duration)
        if expiration_date < datetime.now():
            return None
        return session_dict.get("user_id")
