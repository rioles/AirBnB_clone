#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:

    def __init__(self, *args, **kwargs):
        "Initialize the instance attributes"
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.now()

    def to_dict(self):
        "returns a dic of all keys and values of __dict__"
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        "prints the className, self.id and self.__dict__"
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def save(self):
        "Updates the updated_at with current datetime"
        self.updated_at = datetime.now()

