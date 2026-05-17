from fastapi import FastAPI
import datetime
app = FastAPI()

@app.middleware("http")
async def middleware1(request, call_next):
    print(f"time:{datetime.datetime.now()}")
    response = await call_next(request)
    print(f"time:{datetime.datetime.now()}")
    return response

@app.get("/")
async def root():
    return {"message":"Hello World"}