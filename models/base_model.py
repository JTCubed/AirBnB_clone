#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""

from datetime import datetime
import uuid
# from models import storage


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initiates the BaseModel class"""
        now = datetime.now()
        from models import storage
#        self.id = str(uuid.uuid4())
#        from models import storage

#        self.created_at = now
#        self.updated_at = now

        if kwargs and kwargs != {}:
            for i, j in kwargs.items():
                if i != '__class__':
                    if i == 'created_at' or i == 'updated_at':
                        j = datetime.fromisoformat(j)
                    setattr(self, i, j)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = now
            self.updated_at = now
            storage.new(self)

    def save(self):
        """Updates updated_at attribute"""
        from models import storage
        now = datetime.now()
        self.updated_at = now
        storage.save()

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict


# if __name__ == "__main__":
#    p = BaseModel()
#    a = p.to_dict()
#    o = BaseModel(**a)
