#!/usr/bin/python3
"""This module contains the test cases for the Base Model Class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class BaseModel_Test(unittest.TestCase):
    """Class has test cases for the Base Model"""

    def test_toDict(self):
        """The actual test case"""
        m = BaseModel()
        a_json = m.to_dict()
        self.assertIsInstance(a_json, dict)
        self.assertEqual(a_json['__class__'], 'BaseModel')

    def test_StorageAll(self):
        """Tests whether the all() method returns a dictionary"""
        from models import storage
        self.assertIsInstance(storage.all(), dict)

    def test_Attributes(self):
        """Tests attributes"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

    def test_BaseModelRegen(self):
        """TEsting whether object-regeneration works"""
        g = BaseModel()
        myD = g.to_dict()
        m = BaseModel(**myD)
        self.assertEqual(m.id, g.id)
        self.assertIs(type(m.created_at), datetime)
        self.assertIs(type(m.updated_at), datetime)

    def test_id_unique(self):
        """Test unique id"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)
