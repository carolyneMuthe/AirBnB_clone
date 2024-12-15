#!/usr/bin/python3
"""Unit test for the User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def test_attributes(self):
        """Test user attributes"""
        user = User()
        self.assertEqual(user.email, "")
