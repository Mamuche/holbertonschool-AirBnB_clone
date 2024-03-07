#!/usr/bin/python3
"""Test unittest for class FileStorage"""
import unittest
import json
import os
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
        self.assertEqual(len(all_objects), 2)
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
        """Save the objects to the file"""
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload() method"""
        storage = FileStorage()
        try:
            storage.reload()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        

if __name__ == '__main__':
    unittest.main()
