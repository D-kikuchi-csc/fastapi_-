from pydantic import BaseModel
from typing import List
from datetime import datetime


class login(BaseModel):
    id:str
    password:str



class User(BaseModel):
    id:str
    role:int
    name:str
    password: str
    is_ative:bool
    create_at:datetime
    class Config:
        orm_mode = True

class Test_recive(BaseModel):
    recived_at:datetime
    user_id:str
    test_id:int
    testcase1_point:int
    testcase2_point:int
    testcase3_point:int
    testcase4_point:int
    testcase5_point:int
    total_point:int
    class Config:
        orm_mode = True

class Testbox(BaseModel):
    id:int
    title:str
    quiz:str
    release:int
    class Config:
        orm_mode=True

class UserWithTestbox(User):
    testbox:List[Testbox]=[]

class TestboxWithUser(Testbox):
    admin:User



