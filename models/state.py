#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """a class that identifies which state you are booking in"""


    name: str = ""
