import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def test_all(self):
        p = FileStorage()
        q = p.all()
        self.assertEqual(type(q), dict)

    def test_new(self):
        p = FileStorage()
        obj = BaseModel()
        p.new(obj)
        self.assertEqual(p._FileStorage__objects, {'BaseModel.123': obj})
