#!/usr/bin/python3
"""create class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""
    """__file_path : access road,
    __objects : dictionary containing serialized objects."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for k, obj in self.__objects.items():
            serialized_objects[k] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
            for k, obj_dict in loaded_objects.items():
                class_name, obj_id = k.split('.')
                obj_instance = globals()[class_name](**obj_dict)
                self.__objects[k] = obj_instance
        except FileNotFoundError:
            pass
