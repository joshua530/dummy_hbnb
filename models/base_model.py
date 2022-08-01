#!/usr/bin/python3
"""Contains BaseModel definition"""

import uuid
import datetime

import models


class BaseModel:
    """BaseModel class

    Other models will inherit from this class

    Attributes:
        id: generated id of a new instance
        created_at: time of instance creation
        updated_at: time at which the instance was updated
    """

    def __init__(self, *args, **kwargs):
        """Instantiates a BaseModel instance"""
        # use provided values to instantiate an object
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of a BaseModel object"""
        return "[{}] ({}) <{}>".format(
            self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """Returns standardized string representation of a BaseModel object"""
        return self.__str__()

    def save(self):
        """Saves a BaseModel instance"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts instance to dictionary"""
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime.datetime):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
