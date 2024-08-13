from pydantic import BaseModel, EmailStr


class UserScherma(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDTOScherma(BaseModel):
    username: str
    email: EmailStr
