import unittest
from unittest.mock import patch
from models.base_model import BaseModel
import uuid
from datetime import datetime
import time

class TestsBaseModel(unittest.TestCase):

    @patch('models.base_model.uuid')
    def test_uuid(self, mock_uuid):

        fixed_uuid = uuid.UUID('00000000-0000-0000-0000-000000000001')
        mock_uuid.uuid4.return_value = fixed_uuid

        obj = BaseModel()
        result = obj.id

        self.assertEqual(result, str(fixed_uuid))


    @patch('models.base_model.uuid')
    def test_uuid_is_str(self, mock_uuid):

        fixed_uuid = uuid.UUID('00000000-0000-0000-0000-000000000001')
        mock_uuid.uuid4.return_value = fixed_uuid

        obj = BaseModel()
        result = obj.id

        self.assertEqual(type(result), str)


    def test_created_at_ep_updated_at(self):

        p = BaseModel()
        self.assertEqual(p.created_at, p.updated_at)
        self.assertEqual(type(p.created_at), datetime)



    def test_save(self):
        p = BaseModel()
        time.sleep(0.005)
        p.save()
        self.assertNotEqual(p.created_at, p.updated_at)


    def test_to_dict(self):
        p = BaseModel()
        self.assertEqual(type(p.created_at), datetime)
        o = p.to_dict()
        for key, value in o.items():
            if key == 'created_at':
                self.assertEqual(type(value), str )

    def test_iso(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()
        for key, value in my_model_json.items():
            if key == 'created_at':
                self.assertEqual(type(value), str)
            if key == 'updated_at':
                self.assertEqual(type(value), str)
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(type(my_new_model.created_at), datetime)
        self.assertEqual(type(my_model.created_at), datetime)


        @patch('models.base_model.datetime')
        def test_created_at(self, mock_datetime):
            now = datetime(2017, 9, 28, 21, 5, 54, 119427)

            mock_datetime.datetime.now.return_value = now

            obj = BaseModel()
            result = obj.created_at

            self.assertEqual(result, now)
#        test for __str__






if __name__ == '__main__':
    unittest.main()
