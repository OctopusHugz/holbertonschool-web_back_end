#!/usr/bin/env python3
""" This module implements the Auth class """
from typing import List, TypeVar
from flask import request
import os


class Auth:
    """ Instance of the Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines whether a given path requires auth """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        elif path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p[-1] == "*":
                base_string = p[0:-1]
                if base_string in path:
                    return False
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Returns the value of the header request Authorization """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns a user if that user is authenticated """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from a request """
        if request is None:
            return None
        cookie_name = os.getenv("SESSION_NAME")
        return request.cookies.get(cookie_name)
