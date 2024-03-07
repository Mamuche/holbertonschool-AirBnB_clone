#!/usr/bin/python3
"""Test unittest for class BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test initialization with arguments"""
        obj = BaseModel(id="123", created_at=datetime.now(), updated_at=datetime.now())
        self.assertEqual(obj.id, "123")
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

        """Test initialization without arguments"""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """Test tht str method"""
        obj = BaseModel(id="123")
        expected_output = "[BaseModel] (123) {'id': '123'}"
        self.assertEqual(str(obj), expected_output)

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        obj = BaseModel(id="123", created_at=datetime.now(), updated_at=datetime.now())
        expected_dict = {
            'id': '123',
            '__class__': 'BaseModel',
            'created_at': obj.created_at.isoformat(),
            'updated_at': obj.updated_at.isoformat()
        }
        self.assertDictEqual(obj.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
