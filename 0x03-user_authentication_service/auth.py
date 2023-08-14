#!/usr/bin/env python3
"""
hashing passwords
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """the hashing method"""
    salt = bcrypt.gensalt()

    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pwd
