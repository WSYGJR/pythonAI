from fastapi import FastAPI,Query

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/book")
async def get_book(
        type: str = Query(...,description="图书分类",min_length=5,max_length=255),
        price: int = Query(...,description="图书价格",gt=49,lt=101)
):
    return {"type": type, "price": price}