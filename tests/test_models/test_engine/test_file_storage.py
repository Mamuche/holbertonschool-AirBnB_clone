#!/usr/bin/python3
"""Test unittest for class FileStorage"""
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test fixtures"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up test fixtures"""
        self.storage = None

    def test_all(self):
        """Test the all() method
        Add some objects to the storage"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        """Retrieve all objects from the storage"""
        all_objects = self.storage.all()

        """Check if the objects are retrieved correctly"""
        self.assertIn(obj1, all_objects.values())
        self.assertIn(obj2, all_objects.values())

    def test_new(self):
        """Test the new() method
        Create a new object"""
        obj = BaseModel()

        """Add the object to the storage"""
        self.storage.new(obj)

        """Check if the object is added correctly"""
        self.assertIn(obj, self.storage.all().values())

    def test_save(self):
        """Test the save() method
        Add some objects to the storage"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)

        """Save the objects to the file"""
        self.storage.save()

        """Check if the file is created and contains the serialized objects"""
        with open(self.storage._FileStorage__file_path, 'r') as file:
            loaded_objects = json.load(file)
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", loaded_objects)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", loaded_objects)


if __name__ == '__main__':
    unittest.main()
