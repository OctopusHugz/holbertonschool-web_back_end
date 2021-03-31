#!/usr/bin/env python3
""" This module implements the BasicAuth class """
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.base import DATA
from models.user import User
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
        values = decoded_base64_authorization_header.split(':', 1)
        return values[0], values[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password """
        if user_email is None or not isinstance(user_email, str):
            return None
        elif user_pwd is None or not isinstance(user_pwd, str):
            return None
        elif User.count() == 0 or User.search({"email": user_email}) is None:
            return None
        my_user = User.search({"email": user_email})[0]
        if my_user.is_valid_password(user_pwd):
            return my_user
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Overloads Auth and retrieves the User instance for a request """
        authorization_header = self.authorization_header(request)
        extracted_auth_header = self.extract_base64_authorization_header(
            authorization_header)
        decoded_auth_header = self.decode_base64_authorization_header(
            extracted_auth_header)
        user_creds = self.extract_user_credentials(decoded_auth_header)
        current_user = self.user_object_from_credentials(
            user_creds[0], user_creds[1])
        return current_user
