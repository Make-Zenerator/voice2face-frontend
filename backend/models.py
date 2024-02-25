from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Float, Numeric
from database import Base
from typing import Optional
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True)
    password = Column(String(255))
    age = Column(Integer)
    gender = Column(Boolean) # 0: man, 1: woman
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('USERS.id'))
    age = Column(Integer) # 0: man, 1: woman
    gender = Column(Boolean)
    voice_url = Column(String(255))
    status = Column(Integer)
    eta = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey('REQUESTS.id'))

    condition_image_url = Column(String(255), nullable=True)
    condition_gif_url = Column(String(255), nullable=True)
    voice_image_url = Column(String(255), numllable=True)
    voice_gif_url = Column(String(255), numllable=True)
    
    condition_image_rating = Column(Integer, nullable=True)
    condition_gif_rating = Column(Integer, nullable=True)
    voice_image_rating = Column(Integer, numllable=True)
    voice_gif_rating = Column(Integer, numllable=True)
    
    voice_image_score = Column(Float, nullable=True)
    condition_gif_score = Column(Float, nullable=True)
    voice_image_score = Column(Float, numllable=True)
    voice_gif_score = Column(Float, numllable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

