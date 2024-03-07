#!/usr/bin/python3
"""Test unittest for class Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for class Place"""

    def test_args(self):
        """Test initialization with arguments"""
        place = Place(city_id="123", user_id="456", name="Test Place",
                      description="This is a test place",
                      number_rooms=2, number_bathrooms=1,
                      max_guest=4, price_by_night=100,
                      latitude=37.7749, longitude=-122.4194,
                      amenity_ids=["amenity1", "amenity2"])

        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "This is a test place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == '__main__':
    unittest.main()
