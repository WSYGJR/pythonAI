from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/book/{id}")
async def get_book(id: int = Path(..., gt=0,lt=101)):
    return {"id": id,"title":f"这是第{id}本书"}

#需求：查找书籍的作者，路径参数name，长度范围2-10

@app.get("/author/{name}")
async def get_author(name: str = Path(...,min_length=2,max_length=10)):
    return {"msg": f"这是{name}的信息"}