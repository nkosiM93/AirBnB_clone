#!usr/bin/env python3
"""Tests the Amenity class"""
from models.amenity import Amenity
import unittest
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Tests the Amenity Class"""

    def test_defaultVale(self):
        self.assertEqual(Amenity().name, "")

    def test_attrType(self):
        self.assertIsInstance(Amenity.name, str)

    def test_isSubClass(self):
        self.assertTrue(issubclass(Amenity, BaseModel))
