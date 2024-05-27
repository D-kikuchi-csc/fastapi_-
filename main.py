import stat
from fastapi import Depends, FastAPI, HTTPException,Body, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from functools import lru_cache
from .config import settings



@lru_cache()
def get_settings():
    return settings()




models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://127.0.0.1:8000",
]



# @app.get('/login',response_model=schemas.User)
# def get_user(id:int,password:int):
#     return {'id':id,'password':password}

@app.post("./")
async def receive_form_data(request:Request) -> dict:
    data = await request.json()
    print(data.get("message"))
    return {"Received Data": "OK"}


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Login(BaseModel):
        id:str
        password:str


@app.post("/login",response_model=schemas.User)
async def login(login:Login,db: Session = Depends(get_db)):
    print('postデータを受け取ったので処理します')
    jsondata=jsonable_encoder(login)
    print(jsondata)
    db_user=crud.get_login(db, user_id=login.id, user_pass=login.password)
    user=jsonable_encoder(db_user)
    # print((db_user.role))
    print(user)
    if db_user is None :
        print('該当ユーザがいませんでした')
        return JSONResponse(content={"access":"0"})
    elif db_user.is_active is False:
        print('このユーザは削除されています')
        return JSONResponse(content={"access":"0"})
    elif db_user.role==1:
        print('Adminがログインしました')
        return JSONResponse(content={"access":"2"})
    else:
        print('studentがログインしました')
        return JSONResponse(content={"access":"1"})




@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# @app.get("/users/{user_id}", response_model=schemas.UserWithTestbox)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user



@app.get("/users", response_model=list[schemas.User])
def read_user(db: Session = Depends(get_db)):
    db_user = crud.get_alluser(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/testbox/{id}", response_model=schemas.TestboxWithUser)
def read_textbox(id: int, db: Session = Depends(get_db)):
    db_test =crud.get_test(db,id=id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_test

@app.post("/users/create")
async def create_user(id:int=Body(), name:str=Body(),role:int=Body(),password:str=Body(),db: Session = Depends(get_db)):
    user = models.User(id=id,name=name,role=role,password=password)
    db.add(user)
    db.flush()
    db.commit()
    return

@app.post("/users/update")
async def create_user(id:int=Body(), name:str=Body(),role:int=Body(),password:str=Body(),db: Session = Depends(get_db)):
    user = models.User(id=id,name=name,role=role,password=password)
    db._update_impl(user)
    db.flush()
    db.commit()
    return