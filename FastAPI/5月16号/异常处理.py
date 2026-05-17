from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/news/{id}")
async def fet_news(id:int):
    id_llist=[1,2,3,4,5]
    if id not in id_llist:
        raise HTTPException(status_code=404,detail="没有此id")

    return {f"id:{id}"}