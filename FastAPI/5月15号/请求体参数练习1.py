from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

#注册：用户名和密码-》str
class Library(BaseModel):
    bookname:str
    author:str
    publishment:str
    price: float

@app.post("/library")
async def library(book:Library):
    return book