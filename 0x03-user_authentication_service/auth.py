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


def _generate_uuid() -> str:
    """generating uuids"""
    the_uuid = str(uuid.uuid4())
    return the_uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def get_user(self, email: str) -> User:
        """if user email is registered"""
        try:
            user = self._db.find_user_by(email=email)
            return user
        except NoResultFound:
            return None

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

    def create_session(self, email: str) -> str:
        """returns the session id as str"""
        # user = self._db._session.query(User).filter_by(email=email).first()
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                user.session_id = session_id

                # persisting the session
                try:
                    self._db._session.commit()
                    return session_id
                except Exception as e:
                    self._db._session.rollback()
                    print("Error commiting changes:", e)
                    return None
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """returns the corresponding user or none"""
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            if not user or user is None:
                return None

            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """method updates the corresponding user is to None"""
        try:
            user = self._db.find_user_by(user_id=user_id)
            user.session_id = None
            return None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """generates a reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            if not user or user is None:
                raise ValueError("No user Found")

            reset_token = _generate_uuid()
            user.reset_token = reset_token
        except NoResultFound:
            raise ValueError("No user Found")
        else:
            return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """updating users password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user is None:
                raise ValueError("Not Found")
        except NoResultFound:
            raise ValueError("Not Found")
        else:
            hashed = _hash_password(password)
            user.hashed_password = hashed
            user.reset_token = None
            return None
