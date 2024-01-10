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
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime
                                (value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """human readable string"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts the object's attributes into a dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
