from fastapi import FastAPI,Path

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/{id}")
async def get_id(id :int = Path(..., gt=0,lt=101)):
    return("msg",f"新闻id为{id}")

@app.get("/{id}/{type}")
async def get_type(type :str = Path(..., min_length=2,max_length=10)):
    return("msg",f"新闻分类为{type}")
