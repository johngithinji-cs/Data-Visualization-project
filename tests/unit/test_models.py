#!/usr/bin/env python3
"""Module to test our modles"""

from app.models.user import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the id, name, email and passwords are well defined
    """
    user = User(1, "John", "johndoe@email.com", "password")
    assert user.id == 1
    assert user.name == "John"
    assert user.email == "johndoe@email.com"
    assert user.password != "password"
