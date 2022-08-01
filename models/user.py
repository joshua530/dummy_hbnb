#!/usr/bin/python3
"""Contains user model definition"""
from models.base_model import BaseModel


class User(BaseModel):
    """User model class

    Attributes:
        email: user email
        password: user password
        first_name: user's first name
        last_name: user's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
