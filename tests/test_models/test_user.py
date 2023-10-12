#!/usr/bin/env python3
"""Tests the User class"""
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Tests the user class"""

    def test_defaultVale(self):
        """Test to see what the default values are for te attributes"""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_attributes(self):
        """Tests inf attributes are present"""
        a = User()
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, 'email'))
        self.assertTrue(hasattr(a, 'first_name'))
        self.assertTrue(hasattr(a, 'last_name'))
        self.assertTrue(hasattr(a, 'password'))

    def test_inheritance(self):
        """Test inheritance"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_types(self):
        """Checks the attr types"""
        self.assertTrue(isinstance(User.email, str))
        self.assertTrue(isinstance(User.first_name, str))
        self.assertTrue(isinstance(User.last_name, str))
        self.assertTrue(isinstance(User.password, str))
