#!/usr/bin/python3
""" This module defines a DB Storage for the Data Visualization project. """

from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


class DB:
    """The database class
    """

    def __init__(self) -> None:
        """Instantiates a new DBStorage object
        """
        self._engine = create_engine("mysql+mysqldb://analyst:project
                                      @localhost/user_data")
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
