#!/usr/bin/python3
"""Contains City model definition"""
from models.base_model import BaseModel


class City(BaseModel):
    """City model class

    Attributes:
        state_id: id of a state instance
        name: name of state
    """

    state_id = ""
    name = ""
