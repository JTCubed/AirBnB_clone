#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""


from datetime import datetime
import uuid


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self):
        """Initiates the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.now = datetime.now()
#        self.created_at = now.isoformat()
#        self.updated_at = now.isoformat()
        self.created_at = self.now
        self.updated_at = self.now


    def save(self):
        """Updates updated_at attribute"""
        now = datetime.now()
        self.updated_at = str(now.isoformat())

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def to_dict(self):
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        self.created_at = str(self.now.isoformat())
        self.updated_at = str(self.now.isoformat())
        return inst_dict


#if __name__ == "__main__":
#    p = BaseModel()
#    print(type(p.created_at))
