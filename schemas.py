from pydantic import BaseModel
from typing import List

class BaseBlog(BaseModel):
    title: str
    description: str


class Blog(BaseBlog):

    class Config():
        orm_mode = True



class User(BaseModel):
    username: str
    email: str
    password: str


class ShowUser(BaseModel):
    username: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str




