#!/usr/bin/env python3
""" This module handles encrypting passwords using bcrypt and hashpw """
from bcrypt import gensalt, hashpw
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """ Hashes a password given as argument using hashpw with a random salt"""
    return hashpw(password.encode(), gensalt())
