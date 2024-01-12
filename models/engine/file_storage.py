#!/usr/bin/python3
import json
import os


class FileStorage:
    """A class for serializing and deserializing instances to and from JSON."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return fileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        fileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    instance = eval(class_name)(**value)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
