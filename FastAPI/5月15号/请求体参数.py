from selectors import DefaultSelector

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

#注册：用户名和密码-》str
class User(BaseModel):
    username:str = Field(default="张三",min_length=2,max_length=10,description="用户名，长度要求2-10个字符")
    password:str = Field(default="123456",min_length=6,max_length=20,description="密码，长度要求6-20个字符")

@app.post("/register")
async def register(user:User):
    return user