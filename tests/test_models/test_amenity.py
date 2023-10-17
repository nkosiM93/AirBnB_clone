#!/usr/bin/python3
"""Module for amenity"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """testing amenity for functionality"""

    def test_inherit(self):
        """Check inheritence"""
        a = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(hasattr(a, 'id'))
        self.assertTrue(hasattr(a, 'updated_at'))
        self.assertTrue(hasattr(a, 'created_at'))
        self.assertTrue(hasattr(a, 'name'))

    def test_defaults(self):
        """Check the initial Values"""
        self.assertEqual(Amenity.name, "")

    def test_types(self):
        """Cehck the attribute types"""
        self.assertTrue(isinstance(Amenity.name, str))
