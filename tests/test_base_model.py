import unittest

from models.base_model import BaseModel

class test_BaseModel(unittest.TestCase):

    def test_init(self):
        p = BaseModel()
