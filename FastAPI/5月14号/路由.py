from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user/hello")
async def get_hello():
    return {"msg": "我正在学习 FastAPI"}