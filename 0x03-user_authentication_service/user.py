#!/usr/bin/env python3
"""
creating an sqlalchemy model named user for
a database table named users by using mapping declaration
of sqlalchemy
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """base class which maintains a catalog of classes and
    tables relative to that base"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self) -> str:
        """string reporesentation of the above"""
        return "<User(email='%s',\
            hashed_password='%s',session_id='%s', reset_token='%s')>" % (
            self.email, self.hashed_password, self.session_id,
            self.reset_token)
