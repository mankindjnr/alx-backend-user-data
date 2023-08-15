"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """implementing the add user method"""
        the_user = User(email=email, hashed_password=hashed_password)
        self._session.add(the_user)
        self._session.commit()

        return the_user

    def find_user_by(self, **kwargs) -> User:
        """method takes in arbitrary keyword arg and returns
        first row found in the users table"""
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound("Not Found")
        except InvalidRequestError as e:
            self._session.rollback()
            raise e

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """updating a users credentials"""
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError(f"Invalid argument: {key}")
            self._session.commit()
        except NoResultFound:
            raise NoResultFound("user not found")
        except InvalidRequestError as e:
            self._session.rollback()
            raise e
