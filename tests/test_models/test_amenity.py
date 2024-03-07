#!/usr/bin/python3
"""Test unittest for class Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for class Amenity"""

    def test_args(self):
        """Test initialization of Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
