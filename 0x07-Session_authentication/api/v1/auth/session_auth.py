#!/usr/bin/env python3
""" This module implements the SessionAuth class """
from api.v1.auth.auth import Auth
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
