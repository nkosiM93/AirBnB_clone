#!/usr/bin/env python3
"""File storage module"""
import json
#from models.base_model import BaseModel


class FileStorage:
    """class representation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary """
        dReload = self.reload()
        if not dReload or dReload is None:
            pass
        else:
            for k,v in dReload.items():
                self.__objects[k] = v
        return self.__objects

    def new(self, obj):
        """sets in objects"""
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as w_file:
            json.dump(self.__objects, w_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open (self.__file_path, "r", encoding="utf-8") as r_file:
                return json.load(r_file)
        except(FileNotFoundError):
            pass
