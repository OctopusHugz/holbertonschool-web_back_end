#!/usr/bin/env python3
""" This module handles encrypting passwords using bcrypt and hashpw """
from bcrypt import gensalt, hashpw


def hash_password(password: str) -> bytes:
    """ Hashes a password given as argument using hashpw with a random salt"""
    if not isinstance(password, bytes):
        password = password.encode()
    return hashpw(password, gensalt())
