from pydantic.main import BaseModel
from datetime import datetime
from typing import Dict, Optional, List, Set, Union


class User(BaseModel):
    code: str
    name: str

    @classmethod
    def from_dict(cls, dic: Dict):
        User(**dic)

        return dic

    @classmethod
    def from_to_dict(cls, dic: List):
        User(**list(dic))
        return dic

    @classmethod
    def from_dict_to(cls, dic: Dict):
        User(**dic)
        return dic


class UserList(BaseModel):
    data: List[User]
