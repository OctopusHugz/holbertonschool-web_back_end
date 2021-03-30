#!/usr/bin/env python3
""" This module implements the Auth class """
from typing import List, TypeVar
from flask import request


class Auth:
    """ Instance of the Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines whether a given path requires auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ Returns the value of the header request Authorization """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns a user if that user is authenticated """
        return None
