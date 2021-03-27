#!/usr/bin/env python3
""" This module handles encrypting passwords using bcrypt and hashpw """
from bcrypt import gensalt, hashpw, checkpw
import base64
import hashlib


def hash_password(password: str) -> bytes:
    """ Hashes a password given as argument using hashpw with a random salt"""
    return hashpw(
        base64.b64encode(hashlib.sha256(password.encode()).digest()), gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks whether a hashed password matches a non-hashed password """
    return checkpw(password.encode(), hashed_password)
