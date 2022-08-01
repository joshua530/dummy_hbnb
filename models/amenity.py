#!/usr/bin/python3
"""Contains Amenity class definition"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity entity class

    Attributes:
        name: name of the amenity
    """

    name = ""
