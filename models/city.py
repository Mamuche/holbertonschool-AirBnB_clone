#!/usr/bin/python3
"""create class City"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """class City inherit from BaseModel"""
    state_id = ""
    name = ""
