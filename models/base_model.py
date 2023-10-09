#!/usr/bin/env python3
""" Module contains the Base model class """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The Base model class"""

    def __init__(self):
        """Initialization for the Base Model class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String repr of the Base Model Class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """..."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ 
            Returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        bModelDict = dict(self.__dict__)
        bModelDict['__class__'] = type(self).__name__
        bModelDict['created_at'] = self.created_at.isoformat()
        bModelDict['updated_at'] = self.updated_at.isoformat()
        return bModelDict
