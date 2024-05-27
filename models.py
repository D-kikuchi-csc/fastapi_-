from sqlalchemy import  Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql import func



    
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name=Column(String)
    role=Column(Integer)
    password=Column(String)
    profile=Column(String)
    is_active=Column(Boolean ,default=True)
    create_at=Column(DateTime(timezone=False),default=func.now)

    testbox=relationship("Testbox",back_populates="admin")

class Test_recive(Base):
    __tablename__="test_recive"

    id = Column(Integer, primary_key=True)
    recived_at= Column(DateTime(timezone=True),default=func.now)
    user_id=Column(String)
    total_point=Column(Integer,default=0)
    testcase1_point=Column(Integer,default=0)
    testcase2_point=Column(Integer,default=0)
    testcase3_point=Column(Integer,default=0)
    testcase4_point=Column(Integer,default=0)
    testcase5_point=Column(Integer,default=0)
    test_id=Column(Integer)


class Testbox(Base):
    __tablename__="test_box"

    id=Column(Integer, primary_key=True)
    title=Column(String)
    quiz=Column(String)
    constraints=Column(String)
    sec=Column(Integer)
    upper_memory=Column(Integer)
    in_format=Column(String)
    out_format=Column(String)
    in1=Column(String)
    in2=Column(String)
    out1=Column(String)
    out2=Column(String)
    release=Column(Integer)
    testcase1=Column(String)
    testcase2=Column(String)
    testcase3=Column(String)
    testcase4=Column(String)
    testcase5=Column(String)
    start_time=Column(DateTime)
    finished_time=Column(DateTime)
    create_id=Column(Integer,ForeignKey("users.id"))

    admin=relationship("User",back_populates="testbox")