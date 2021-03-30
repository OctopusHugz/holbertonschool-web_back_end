#!/usr/bin/env python3
""" This module implements the BasicAuth class """
from typing import Tuple
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Instance of the BasicAuth class, which inherits from Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns Base64 of Authorization header for Basic Authentication"""
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Returns decoded value of base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        try:
            if base64.b64encode(
                    base64.b64decode(base64_authorization_header)
            ) == base64_authorization_header:
                pass
        except Exception:
            return None
        decoded_string = base64.b64decode(base64_authorization_header)
        return decoded_string.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """Returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        elif not isinstance(decoded_base64_authorization_header, str):
            return None, None
        elif ":" not in decoded_base64_authorization_header:
            return None, None
        values = decoded_base64_authorization_header.split(':')
        return values[0], values[1]
