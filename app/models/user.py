#!/usr/bin/env python3
"""Module for a SQLAlchemy model named User for a database table named users.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from .. import db


#Base = declarative_base()


class User(db.Model):
    """Model for a database table users."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    username = Column(String(250), nullable=True)
    hashed_password = Column(String(250), nullable=False)
