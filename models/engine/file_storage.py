#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file
to instances:
"""

import os
from models.base_model import BaseModel
import json
from models.user import User


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances:
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        ets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(serialized, f)


    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing
        """
        from models.base_model import BaseModel
        try:
            if os.path.getsize(self.__file_path) > 0:
                with open(self.__file_path, 'r') as f:
                    o = json.load(f)
                    for key, value in o.items():
                        class_name = value['__class__']

                        class_ = globals().get(class_name, BaseModel)

                        if not issubclass(class_, BaseModel):
                            class_ = BaseModel

                        obj_instance = class_(**value)
                        self.__objects[key] = obj_instance

        except FileNotFoundError:
            pass
#        except json.decoder.JSONDecodeError:
#            pass


#if __name__ == '__main__':
#    o = FileStorage()
#    j = {}
#    o.reload()
#    print(o.all())
