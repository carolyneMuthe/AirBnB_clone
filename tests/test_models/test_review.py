#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance(self):
        """Test if object is an instance of Review."""
        review = Review()
        self.assertIsInstance(review, Review)


if __name__ == "__main__":
    unittest.main()
