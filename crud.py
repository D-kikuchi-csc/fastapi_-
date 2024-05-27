from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_login(db: Session, user_id: str,user_pass:str):
    return db.query(models.User).filter(models.User.id == user_id, models.User.password == user_pass).first()

def get_alluser(db: Session):
    return db.query(models.User).all()

def get_result(db:Session,user_id:int):
    return db.query(models.Test_recive).filter(models.Test_recive.id == user_id).first()

def get_test(db: Session, id: int):
    return db.query(models.Testbox).filter(models.Testbox.id == id).first()
