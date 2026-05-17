from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse,FileResponse
import os
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

#HTML响应
@app.get("/html",response_class=HTMLResponse)
async def get_html():
    return "<h1>这是一级标题<h1>"
@app.get("/file")
async def get_file():
    path = r"D:\WORKSPACE\pythonlearning\pythonAI\FastAPI\5月16号\111_file.py"
    if not os.path.exists(path):
        raise HTTPException(status_code=404,detail="没有此文件")
    return FileResponse(path)