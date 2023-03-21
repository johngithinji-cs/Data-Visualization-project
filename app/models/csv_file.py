#!/usr/bin/env python3
"""Module defining csv file table"""

from ..db import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class CSVFile(UserMixin, db.Model):
    """Model for a database table CSV files."""
    __tablename__ = 'csv_files'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.String(100), nullable=False)
    file_data = db.Column(db.LargeBinary, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    # user = relationship('User', back_populates='csv_files')
