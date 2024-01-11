#!/usr/bin/python3
from models.base_model import baseModel


class user(BaseModel):
    """a class representing a user in the application"""


    email = ""
    password = ""
    first_name = ""
    last_name = ""
