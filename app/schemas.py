from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    user_id: int

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    username: str
    user_id: int

class UserList(BaseModel):
    users: list[UserOut]


class Login(BaseModel):
    username: str
    password: str