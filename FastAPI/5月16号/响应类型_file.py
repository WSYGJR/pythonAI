from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/file")
async def get_file():
    return FileResponse(r"D:\WORKSPACE\pythonlearning\pythonAI\FastAPI\5月16号\响应类型_file.py")