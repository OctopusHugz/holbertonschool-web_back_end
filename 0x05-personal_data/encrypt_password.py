#!/usr/bin/env python3
""" This module handles encrypting passwords using bcrypt and hashpw """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes a password given as argument using hashpw with a random salt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks whether a hashed password matches a non-hashed password """
    return bcrypt.checkpw(password.encode(), hashed_password)
