from typing import List

from pydantic import BaseModel

from clinica.src.schemas.users.user_schema import UserSchema


class UserList(BaseModel):
    users: List[UserSchema]
