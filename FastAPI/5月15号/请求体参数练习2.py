from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

#注册：用户名和密码-》str
class Library(BaseModel):
    bookname:str = Field(default = "无标题图书",description="图书名称",min_length=2,max_length=20)
    author:str = Field(...,description="作者名称",min_length=2,max_length=10)
    publishment:str = Field(default="黑马出版社",description="出版社名称")
    price: float = Field(...,description="图书价格",gt=0)

@app.post("/library")
async def library(book:Library):
    return book