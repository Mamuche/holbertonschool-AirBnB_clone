#!/usr/bin/python3
"""Test unittest for class City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for class City"""

    def test_args(self):
        """Test initialization of City instance"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
