#!/usr/bin/env python3
"""
hashing passwords
"""
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


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

    def valid_login(self, email: str, password: str) -> bool:
        """check the password with bcrypt.checkpw"""
        user = self._db._session.query(User).filter_by(email=email).first()
        if user:
            hashed = user.hashed_password
            if bcrypt.checkpw(password.encode('utf-8'), hashed):
                return True
            else:
                return False
        else:
            return False

    def _generate_uuid(self) -> str:
        """generating uuids"""
        the_uuid = str(uuid.uuid4())
        return the_uuid

    def create_session(self, email: str) -> str:
        """returns the session id as str"""
        # user = self._db._session.query(User).filter_by(email=email).first()
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = self._generate_uuid()
                user.session_id = session_id

                return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """returns the corresponding user or none"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            if user is None or session_id is None:
                return None

            return user
        except NoResultFound:
            return None
