#!/usr/bin/python3
"""Module for User"""
from models.base_model import BaseModel


class User(BaseModel):
    """clas user inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
