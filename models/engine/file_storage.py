#!/usr/bin/env python3
"""File storage module"""
import json
#from models.base_model import BaseModel


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
        print(self.__objects)

    def save(self):
        """serializes __objects to the JSON file """
        save_dict = {}
        for i, j in self.__objects.items():
            #save_dict[i] = self.__objects[i].to_dict()
            save_dict[i] = j.to_dict()
        with open(self.__file_path, "a", encoding="utf-8") as w_file:
            json.dump(save_dict, w_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open (self.__file_path, "r", encoding="utf-8") as r_file:
                for line in r_file:
                    read = json.load(r_file)
                    print(read)
        except(FileNotFoundError, json.JSONDecodeError):
            pass
