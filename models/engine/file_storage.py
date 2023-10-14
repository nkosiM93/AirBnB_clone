#!/usr/bin/env python3
"""File storage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.city import City


class FileStorage:
    """class representation"""
    __file_path = "file.json"
    __objects = {}

    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
                }

    def all(self):
        """returns dictionary """
        return self.__objects

    def new(self, obj):
        """sets in objects"""
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        __tempD = {}
        for k, v in self.__objects.items():
            __tempD[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as w_file:
            json.dump(__tempD, w_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as r_file:
                __tempD = json.load(r_file)
                self.__objects.clear()
                for k, v in __tempD.items():
                    self.__objects[k] = FileStorage.classes[v['__class__']](**v)
        except(FileNotFoundError):
            pass
