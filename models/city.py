#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """infor about which city are you in"""


    state_id: str = ""
    name: str = ""
