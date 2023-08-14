#!/usr/bin/env python3
"""
hashing passwords
"""
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


def _hash_password(password: str) -> bytes:
    """the hashing method"""
    salt = bcrypt.gensalt()

    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """returns a user object"""
        if self._db._session.query(User).filter_by(email=email).first():
            raise ValueError(f"User {email} already exists")
        _passwd = _hash_password(password)

        user = User(email=email, hashed_password=_passwd)
        self._db.add_user(email, _passwd)
        return user
