#!/usr/bin/env python3
""" This module handles encrypting passwords using bcrypt and hashpw """
from bcrypt import checkpw, gensalt, hashpw


def hash_password(password: str) -> bytes:
    """ Hashes a password given as argument using hashpw with a random salt"""
    if isinstance(password, str):
        return hashpw(password.encode(), gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks whether a hashed password matches a non-hashed password """
    if isinstance(password, str) and isinstance(hashed_password, bytes):
        return checkpw(password.encode(), hashed_password)
