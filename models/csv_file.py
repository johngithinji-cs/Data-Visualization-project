#!/usr/bin/env python3
"""Module for a SQLAlchemy model named User for a database table named csv files.
"""

from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, DateTime
from sqlalchemy.orm import relationship


Base = declarative_base()


class CSVFile(Base):
    """Model for a database table CSV files."""
    __tablename__ = 'csv_files'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    filename = Column(String(100), nullable=False)
    file_data = Column(LargeBinary, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    user = relationship('User', back_populates='csv_files')


