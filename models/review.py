#!/usr/bin/python3
"""create class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review inherit from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
