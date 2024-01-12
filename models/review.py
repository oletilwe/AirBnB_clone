#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """to leave a review"""

    def __init__(self):
        super().__init__()
        self.name = ""

    def to_dict(self):
        state_dict = super().to_dict()
        state_dict.update({
            "name": self.name,
        })
        return state_dict

    def from_dict(self, data):
        super().from_dict(data)
        self.name = data.get("name", "")

    place_id: str = ""
    user_id: str = ""
    text: str = ""
