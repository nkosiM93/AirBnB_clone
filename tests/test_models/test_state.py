#!/usr/bin/python3
"""Test for State class"""
import unittest
import models
from models.state import State
from models import BaseModel


class TestState(unittest.TestCase):
    """Test case for state classes """
    def test_inherit(self):
        """to test whether it inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_attr_creation(self):
        """to test whether attributes are present"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
    def test_type(self):
        """test for value type"""
        state = State()
        self.assertTrue(type(state.name) == str)


if __name__ == "__main__":
    unittest.main()
