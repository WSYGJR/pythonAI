from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

#HTML响应
@app.get("/html",response_class=HTMLResponse)
async def get_html():
    return "<h1>这是一级标题<h1>"