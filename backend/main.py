from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from datetime import datetime
from databases import Database
from passlib.context import CryptContext
from typing import Optional, Annotated
import os

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    email: str
    password: str
    age: int
    gender: bool
    updated_at: Optional[datetime]

class RequestBase(BaseModel):
    user_id: int
    age: int
    gender: bool
    voice: str
    status: int
    eta: Optional[datetime]
    updated_at: Optional[datetime]
    
class ResultBase(BaseModel):
    request_id: int
    condition_image_url: Optional[str]
    condition_gif_url: Optional[str]
    voice_image_url: Optional[str]
    voice_gif_url: Optional[str]
    condition_image_rating: Optional[int]
    condition_gif_rating: Optional[int]
    voice_image_rating: Optional[int]
    voice_gif_rating: Optional[int]
    condition_image_score: Optional[float]
    condition_gif_score: Optional[float]
    voice_image_score: Optional[float]
    voice_gif_score: Optional[float]
    updated_at: Optional[datetime]
    

DATABASE_URL = "mysql://root:1234@localhost/MZ"
database = Database(DATABASE_URL)

# 정적 파일 디렉토리 연결
app.mount("/static", StaticFiles(directory="static"), name="static")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

# class User(BaseModel):
#     email: str = Field(..., example="user@example.com")
#     password: str = Field(..., example="password")
#     gender: Optional[str] = Field(None, example="Man")
#     age: Optional[int] = Field(None, example=30)
#     image_path: Optional[str] = Field(None, example="../src/output/image.jpg")

class User(BaseModel):
    email: str = Field(..., example="user@example.com")
    password: str = Field(..., example="example123")
    age: int = Field(..., example=25)
    gender: int = Field(..., example=0)  # 0: man, 1: woman
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None



@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/")
async def create_user(user: User):
    hashed_password = hash_password(user.password)
    query = """
    INSERT INTO user(email, password, gender, age)
    VALUES (:email, :password, NULL, NULL)
    """
    values = {
        "email": user.email,
        "password": hashed_password
    }
    await database.execute(query, values)
    return {"message": "User created successfully."}


@app.post("/login")
async def check_email(user: User):
    hashed_password = hash_password(user.password)
    query = """
    SELECT email, password FROM user
    WHERE email = :email
    """
    values = {
        "email": user.email
    }
    result = await database.fetch_one(query, values)
    if hashed_password == result["password"]:
        return True
    else:
        return {"message": "User password not correct."}

@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        with open('./static/main.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="HTML file not found")
    
@app.get("/get_user_data", response_model=User)
async def get_user_data(email: str):
    query = """
    SELECT * FROM user
    WHERE email = :email
    """
    values = {"email": email}
    result = await database.fetch_one(query, values)
    if result:
        return User(email=result["email"], password=result["password"], gender=result["gender"], age=result["age"])
    else:
        raise HTTPException(status_code=404, detail="User not found")
    

class UserUpdate(BaseModel):
    gender: str
    age: int

@app.post("/update_user_information/{email}")
async def update_user_information(email: str, user_update: UserUpdate):
    print('email: ', email, ' input: ', user_update)
    query = """
    UPDATE user
    SET gender = :gender, age = :age
    WHERE email = :email
    """
    values = {
        "email": email,
        "gender": user_update.gender,
        "age": user_update.age
    }

    await database.execute(query, values)
    
    # 업데이트된 정보를 반환
    return {"email": email, "gender": user_update.gender, "age": user_update.age}
