#!/usr/bin/env python3
"""Module defining our user model"""

from ..db import db
from flask_login import UserMixin


# User Model
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self):
        return f'<User {self.name!r}>'