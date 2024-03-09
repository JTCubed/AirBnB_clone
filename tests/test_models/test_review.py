#!/usr/bin/python3
"""Defines unittests for models/review.py"""


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_01_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_02_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_03_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_04_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_05_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_06_two_reviews_unique_ids(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_07_two_reviews_different_created_at(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_08_two_reviews_different_updated_at(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    def test_09_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = dt
        rev_str = rev.__str__()
        self.assertIn("[Review] (123456)", rev_str)
        self.assertIn("'id': '123456'", rev_str)
        self.assertIn("'created_at': " + dt_repr, rev_str)
        self.assertIn("'updated_at': " + dt_repr, rev_str)

    def test_10_args_unused(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_11_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rev = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rev.id, "345")
        self.assertEqual(rev.created_at, dt)
        self.assertEqual(rev.updated_at, dt)

    def test_12_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReviewSave(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    @classmethod
    def setUp(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_01_one_save(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        self.assertLess(first_updated_at, rev.updated_at)

    def test_02_two_saves(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        second_updated_at = rev.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rev.save()
        self.assertLess(second_updated_at, rev.updated_at)

    def test_03_save_with_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_04_save_updates_file(self):
        rev = Review()
        rev.save()
        rev_id = "Review." + rev.id
        with open("file.json", "r") as f:
            self.assertIn(rev_id, f.read())


class TestReviewToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_01_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_02_to_dict_contains_correct_keys(self):
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_03_to_dict_contains_added_attributes(self):
        rev = Review()
        rev.middle_name = "Holberton"
        rev.my_number = 98
        self.assertEqual("Holberton", rev.middle_name)
        self.assertIn("my_number", rev.to_dict())

    def test_04_to_dict_datetime_attributes_are_strs(self):
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertEqual(str, type(rev_dict["id"]))
        self.assertEqual(str, type(rev_dict["created_at"]))
        self.assertEqual(str, type(rev_dict["updated_at"]))

    def test_05_to_dict_output(self):
        current_datetime = datetime.today()
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = current_datetime
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': current_datetime.isoformat(),
            'updated_at': current_datetime.isoformat(),
        }
        self.assertDictEqual(rev.to_dict(), tdict)

    def test_06_contrast_to_dict_dunder_dict(self):
        rev = Review()
        self.assertNotEqual(rev.to_dict(), rev.__dict__)

    def test_07_to_dict_with_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)


if __name__ == "__main__":
    unittest.main()
