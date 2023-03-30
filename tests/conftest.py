#!/usr/bin/env python3
"""Module to define fixtures"""

from app.models.user import User
from app import app
import pytest


@pytest.fixture(scope='module')
def test_client():
    """
    Create a test client using a context manager
    """
    flask_app = app

    with flask_app.test.client() as testing_client:
        with flask_app.app_context():
            yield testing_client

            
@pytest.fixture(scope='module')
def new_user():
    user = User(1, "John", "johndoe@email.com", "password")
    return user