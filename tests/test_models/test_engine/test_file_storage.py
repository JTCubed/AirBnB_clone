import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def test_all(self):
        p = FileStorage()
        q = p.all()
        self.assertEqual(type(q), dict)
