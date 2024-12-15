#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance(self):
        """Test if object is an instance of City."""
        city = City()
        self.assertIsInstance(city, City)


if __name__ == "__main__":
    unittest.main()
