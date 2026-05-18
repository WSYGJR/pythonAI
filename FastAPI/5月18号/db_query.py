from datetime import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends
from sqlalchemy import String, Float, DateTime, select
from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# 修正数据库 URL
ASYNC_DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3306/fastapi?charset=utf8"

async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20,
)

class Base(DeclarativeBase):

    create_time: Mapped[datetime] = mapped_column(DateTime, default=func.now, comment="创建时间")
    update_time: Mapped[datetime] = mapped_column(DateTime, default=func.now, onupdate=func.now, comment="更新时间")

class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍ID")
    bookname: Mapped[str] = mapped_column(String(255), comment="书名")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")
    price: Mapped[float] = mapped_column(Float, comment="价格")

async def create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):   # 函数名建议用 lifespan，但可以随意
    # 启动时执行
    await create_table()   # 加上 await
    yield
    # 关闭时可以在这里清理资源（可选）

# 将 lifespan 传给 FastAPI
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}


#需求：查询功能的接口，查询图书-》依赖注入：创建依赖项获取数据库会话+Depends注入路由处理函数
#创建异步数据库会话
AsyncSessionLocal = async_sessionmaker(
    bind= async_engine, #绑定数据库引擎
    class_=AsyncSession,#指定会话类
    expire_on_commit=False,#提交后会话不过期，不重新查询数据库
)
#依赖项,用于获取数据库会话
async def get_database():
    async with AsyncSessionLocal() as session:
        try:
            yield session #返回数据库会话给路由处理函数
            await session.commit()#提交事务
        except Exception:
            await session.rollback()#异常，回滚事务
            raise
        finally:
            await session.close()#关闭会话

#普通查询
# @app.get("/book/books")
# async def get_book_list(db: AsyncSession = Depends(get_database)):
#     #查询
#     result = await db.execute(select(Book))#查询，返回一个ORM对象
#     book = result.scalars().all() #查询所有
#     book =  result.scalars().first()#获取第一个
#     book = await db.get(Book, 3)#获取单条数据，根据主键查询
#     return book


#条件查询-比较判断
@app.get("/book/get_book/{book_id}")
async def get_book_list(book_id:int,db:AsyncSession = Depends(get_database)):
    result = await db.execute(select(Book).where(Book.id >= book_id))
    book = result.scalar_one_or_none()
    return book

#条件查询-比较判断
@app.get("/book/search_book")
async def get_book_list(book_price:int,db:AsyncSession = Depends(get_database)):
    result = await db.execute(select(Book).where(Book.price >= book_price))
    book = result.scalars().all()
    return book

#条件查询-模糊查询
@app.get("/book/search_book_like")
async def get_book_list_like(db:AsyncSession = Depends(get_database)):
    # result = await db.execute(select(Book).where(Book.author.like("曹%")))
    # result = await db.execute(select(Book).where((Book.author.like("曹%")) | (Book.price >= 50)))
    #查数据库里的id如果在书籍id列表内就返回
    id_list = [1,3,5,7,9]
    result = await db.execute(select(Book).where((Book.id.in_(id_list))))
    book = result.scalars().all()
    return book

#聚合查询
@app.get("/book/count")
async def get_count(db:AsyncSession = Depends(get_database)):
    result = await db.execute(select(func.count(Book.id)))
    count = result.scalar()
    return count

@app.get("/book/max")
async def get_max(db:AsyncSession = Depends(get_database)):
    result = await db.execute(select(func.max(Book.price)))
    count = result.scalar()
    return count

#分页查询
@app.get("/book/get_books")
async def get_books(
        page:int = 1,
        page_size:int = 3,
        db:AsyncSession = Depends(get_database)
):
    skip = (page - 1) * page_size
    result = await db.execute(select(Book).offset(skip).limit(page_size))
    books = result.scalars().all()
    return books