#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance(self):
        """Test if object is an instance of BaseModel."""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_save(self):
        """Test the save method of BaseModel."""
        base_model = BaseModel()
        base_model.save()
        self.assertTrue(base_model.updated_at > base_model.created_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        base_model = BaseModel()
        base_dict = base_model.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIn("id", base_dict)
        self.assertIn("created_at", base_dict)
        self.assertIn("updated_at", base_dict)


if __name__ == "__main__":
    unittest.main()
