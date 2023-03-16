from sqlalchemy import Column, Integer, String
from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repre__(self):
        return f'<User {self.name!r}>'
