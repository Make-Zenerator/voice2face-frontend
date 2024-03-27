from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from databases import Database
from passlib.context import CryptContext
from typing import Optional
import os

app = FastAPI()

DATABASE_URL = "mysql://root:1234@localhost/MZ"
database = Database(DATABASE_URL)

# 정적 파일 디렉토리 연결
app.mount("/static", StaticFiles(directory="static"), name="static")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

class User(BaseModel):
    email: str = Field(..., example="user@example.com")
    password: str = Field(..., example="password")
    gender: Optional[str] = Field(None, example="Man")
    age: Optional[int] = Field(None, example=30)
    image_path: Optional[str] = Field(None, example="../src/output/image.jpg")

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
