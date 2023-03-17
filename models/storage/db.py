#!/usr/bin/python3
""" This module defines a DB Storage for the Data Visualization project. """

from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """The database class
    """

    def __init__(self) -> None:
        """Instantiates a new DBStorage object
        """
        self._engine = create_engine("mysql+mysqldb://analyst:project\
                                      @localhost/user_data")
        
        Base = declarative_base()
        
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

    def add_user(self, email: str, hashed_password: str,
                 username: str = None) -> User:
        """A function to add a new user to the database
        Args: email
              hashed_password
              username: Optional
        Return: The new user object
        """
        try:
            new_user = User(email=email, hashed_password=hashed_password,
                            username=username)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """It takes arbitrary keyword arguments and uses it to query
        the database
        Return: User object corresponding to the search key.
        """
        for key in kwargs:
            if key not in User.__dict__:
                raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """A function to update user information in the event of
        a change
        Args: user_id
              kwargs: Dictionary of information to change
        """
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise ValueError
        for key, val in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, val)
            else:
                raise ValueError
        self._session.commit()
