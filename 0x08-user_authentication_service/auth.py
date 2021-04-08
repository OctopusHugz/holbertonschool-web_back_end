#!/usr/bin/env python3
""" This module creates auth methods """
import bcrypt


def _hash_password(password: str) -> str:
    """ Hashes a plaintext password using bcrypt.hashpw """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
