#!/usr/bin/env python3
""" This module implements the Auth class """
from typing import List, TypeVar
from flask import request


class Auth:
    """ Instance of the Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines whether a given path requires auth """
        if path is None:
            return True
        elif excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Returns the value of the header request Authorization """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns a user if that user is authenticated """
        return None
