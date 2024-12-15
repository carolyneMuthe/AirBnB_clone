#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_instance(self):
        """Test if object is an instance of State."""
        state = State()
        self.assertIsInstance(state, State)


if __name__ == "__main__":
    unittest.main()
