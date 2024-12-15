#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_all(self):
        """Test the all method of FileStorage."""
        fs = FileStorage()
        all_objects = fs.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test the new method of FileStorage."""
        fs = FileStorage()
        fs.new("test_key", "test_value")
        all_objects = fs.all()
        self.assertIn("test_key", all_objects)

    def test_save(self):
        """Test the save method of FileStorage."""
        fs = FileStorage()
        fs.save()
        # Ensure that no errors are raised and files are saved as expected.
        self.assertTrue(True)  # This is a placeholder; you can add actual validation for file saving.


if __name__ == "__main__":
    unittest.main()
