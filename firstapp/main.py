from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import random

class User(BaseModel):
    name: str
    age: Optional[int] = None
    gender: str
    phone: Optional[str] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user/{name}")
async def read_name(name):
    return {"user name": name}

@app.get("/user/")
async def create_user_id(start: int, end: int):
    return {"user id": random.randint(start,end)}

@app.post("/user/")
async def create_user(user: User):
    return user

@app.get("/user/id/{id}")
async def read_name(id: int):
    return {"user id": id}