#!/usr/bin/python3

import sys
sys.path.insert(0, '/home/idriss/AirBnB_clone/')
from datetime import datetime
from models.base_model import BaseModel
import unittest

# We called the sys function to enable the funtion to import outside the folder



class TestBaseModel(unittest.TestCase):

    def test_id_type(self):
        "Check if the ID is a string"
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_type(self):
        "check the type of the created_at attribute"
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_type(self):
        "check the type of the updated_at attribute"
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_to_dict(self):
        "check the formats of the attributes as well as the return type"
        self.assertEqual(dict, type(BaseModel().to_dict()))


if __name__ == "__main__":
    unittest.main()
