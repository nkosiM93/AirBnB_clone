#!/usr/bin/env python3
"""File storage module"""
import json
from models.base_model import BaseModel

class FileStorage:
    """class representation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary """
        return self.__objects

    def new(self, obj):
        """sets in objects"""
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        __tempD = {}
        for k,v in self.__objects.items():
            __tempD[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as w_file:
            json.dump(__tempD, w_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as r_file:
                __tempD = json.load(r_file)
                self.__objects.clear() # just to make sure it's empty
                for k, v in __tempD.items():
                    #we are storing instances back in __objects, passing values obtained as kwargs because their in a dictionary format
                    #v is the dictionary representing the object's attributes.
                    self.__objects[k] = BaseModel(**v)
        except(FileNotFoundError):
            pass
