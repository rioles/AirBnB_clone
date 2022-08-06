#!/usr/bin/python3
"""
class file storage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path
    __objects = {}

    def all(self):
        """
        Return the dictionary __object
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Set in __objects obj with key <obj_class_name>.id"""
        object_class_name = obj.__class__.name
        id_object = obj.id
        FileStorage.__objects[f'{object_class_name}.{id_object}'] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        object_dict = FileStorage.__objects
        dict_to_dump = {}
        for key, value in object_dict.items():
            if value:
                dict_to_dump[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            json.dump(dict_to_dump, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as q:
                json.load(q)
        except FileNotFoundError:
            return
