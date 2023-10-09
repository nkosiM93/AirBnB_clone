#!/usr/bin/env python3
"""This module contains the test cases for the Base Model Class"""
import unittest
from models.base_model import BaseModel


class BaseModel_Test(unittest.TestCase):
    """Class has test cases for the Base Model"""

    def test_toDict(self):
        """The actual test case"""
        m = BaseModel()
        a_json = m.to_dict()
        self.assertIsInstance(a_json, dict)

    def test_Attributes(self):
        """Tests attributes"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))
