from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app = FastAPI()

class Book(BaseModel):
    id: int = Field(None, description="图书唯一ID，自动生成")
    title: str = Field(..., min_length=1, description="书名")
    author: str = Field(..., min_length=1, description="作者")

books_list = []
current_id = 1  # 自增ID
book = {"id": 1, "title": None, "author":None}

def find_book_index(book_id: int) -> int:
    """根据ID查找图书在列表中的索引，若不存在返回 -1"""
    for item in books_list:
        if item.id == book_id:
            return item.id
    return -1
@app.get("/")
async def root():
    return {"message": "图书管理 API"}
@app.get("/books/")
async def get_all_books():
    """返回所有图书的列表"""
    return books_list

@app.post("/books/")
async def create_book(title: str, author: str):
    """创建一本新图书（ID自动生成）"""
    global current_id
    book["id"]= current_id
    current_id += 1
    book["title"] = title
    book["author"] = author
    books_list.append(book)
    return book

@app.put("/books/{book_id}",)
async def update_book(book_id: int, updated_title: str, updated_author: str):
    """完全替换指定ID的图书信息"""
    idx = find_book_index(book_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="图书不存在")
    # 保持原ID不变，更新其他字段
    books_list[idx].title = updated_title
    books_list[idx].author = updated_author
    return books_list

# DELETE /books/{book_id} - 删除图书
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """删除指定ID的图书"""
    idx = find_book_index(book_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="图书不存在")
    books_list.pop(idx)