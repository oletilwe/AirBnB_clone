#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """this is the class that the whole project is based off"""

    def __init__(self, *args, **kwargs):
        """this is where the uuid is created"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """human readable string"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """updates the updated_at"""
        self.updated_at = datetime.now()
        models.storage.new()

    def to_dict(self):
        """Converts the object's attributes into a dictionary"""
        result = dict(self.__dict__)
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
