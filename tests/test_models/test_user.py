#!/usr/bin/python3
"""Test unittest for class User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_args(self):
        """Test initialization with arguments"""
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_default_values(self):
        """Test initialization with default values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
