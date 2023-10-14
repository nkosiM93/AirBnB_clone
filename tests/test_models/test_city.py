#!/usr/bin/python3
"""City Tester module"""
from models.base_model import BaseModel
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class tests the City class"""

    def test_inheritance(self):
        """Test if inheritance happens well"""
        ci = City()
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(hasattr(ci, 'id'))
        self.assertTrue(hasattr(ci, 'created_at'))
        self.assertTrue(hasattr(ci, 'updated_at'))
        self.assertTrue(hasattr(ci, 'name'))
        self.assertTrue(hasattr(ci, 'state_id'))

    def test_defaults(self):
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_types(self):
        """Tests what types of attributes we have"""
        self.assertTrue(isinstance(City.name, str))
        self.assertTrue(isinstance(City.state_id, str))
