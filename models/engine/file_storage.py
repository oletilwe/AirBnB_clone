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
        save_dict = {}
        for key, value in fileStorage.__objects.items():
            save_dict[key] = value.to_dict()
        with open(fileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(save_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
        with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                load_dict = json.load(f)
                for key, value in load_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
