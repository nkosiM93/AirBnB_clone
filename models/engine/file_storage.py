#!/usr/bin/env python3
"""File storage module"""
import json

class FileStorage:
    """class representation"""
    __file_path = "file.json"
    __objects = {}

    def  all(self):
        """returns dictionary """
        return self.__objects

    def new(self, obj):
        """sets in objects"""
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file """
        with open(self.__file_path, "w", encoding="utf-8") as w_file:
            json.dump(self.__objects, w_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open (self.__file_path, "r", encoding="utf-8") as r_file:
                return json.loads(r_file)
        except(FileNotFoundError):
            pass
