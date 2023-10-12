#!/usr/bin/python3
"""Module for Review testing"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Class that tests the Review class"""

    def test_inherit(self):
        """Tests inheritence"""
        r = Review()
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(hasattr(r, 'id'))
        self.assertTrue(hasattr(r, 'created_at'))
        self.assertTrue(hasattr(r, 'updated_at'))
        self.assertTrue(hasattr(r, 'place_id')) 
        self.assertTrue(hasattr(r, 'user_id'))
        self.assertTrue(hasattr(r, 'text'))

    def test_Values(self):
        """Tests if values are correct type"""
        self.assertTrue(isinstance(Review.place_id, str))
        self.assertTrue(isinstance(Review.user_id, str))
        self.assertTrue(isinstance(Review.text, str))
