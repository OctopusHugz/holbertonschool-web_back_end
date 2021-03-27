#!/usr/bin/env python3
""" This module handles encrypting passwords """
from typing import ByteString
from bcrypt import gensalt, hashpw


def hash_password(password: str) -> ByteString:
    """ Hashes a password given as argument """
    return hashpw(password.encode(), gensalt())
