#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_instance(self):
        """Test if object is an instance of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == "__main__":
    unittest.main()
