#!/usr/bin/env python3
""" This module handles encrypting passwords using bcrypt and hashpw """
from bcrypt import gensalt, hashpw


def hash_password(password: str) -> bytes:
    """ Hashes a password given as argument using hashpw with a random salt"""
    return hashpw(password.encode(), gensalt())
