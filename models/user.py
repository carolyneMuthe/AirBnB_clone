#!/usr/bin/python3
"""User module"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines a User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
