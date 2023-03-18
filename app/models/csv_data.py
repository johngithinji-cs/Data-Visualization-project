#!/usr/bin/env python3
"""Module for a SQLAlchemy model named User for a database table named CSV data.
"""

import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary, DateTime,  ForeignKey, Table
from sqlalchemy.orm import relationship


Base = declarative_base()


class CSVData(Base):
    """Model for a database table csv data."""
    __tablename__ = 'csv_data'
    id = Column(Integer, primary_key=True)
    csv_file_id = Column(Integer, ForeignKey('csv_files.id'), nullable=False)
    row_index = Column(Integer, nullable=False)
    column_1 = Column(String(50), nullable=False)
    column_2 = Column(String(50), nullable=False)
    # ...
    column_n = Column(String(50), nullable=False)
    csv_file = relationship('CSVFile', backref='csv_data')
 
   