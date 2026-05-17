from datetime import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends
from sqlalchemy import String, Float, DateTime, select
from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3306/menu?charset=utf8"

async_engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20,
)

class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, default=func.now, comment="创建时间")
    update_time: Mapped[datetime] = mapped_column(DateTime, default=func.now, onupdate=func.now, comment="更新时间")

class Menu(Base):
    __tablename__ = "menu"
    id: Mapped[int] = mapped_column(primary_key=True, comment="菜单ID")
    name: Mapped[str] = mapped_column(String(255), comment="菜品名称")
    price: Mapped[float] = mapped_column(Float, comment="价格")
    description: Mapped[str] = mapped_column(String(255), comment="描述")
    image_url: Mapped[str] = mapped_column(String(255), comment="图片URL")

async def create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    await create_table()
    yield

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

@app.get("/menus")
async def get_menu(db: AsyncSession = Depends(get_database)):
    #查询
    result = await db.execute(select(Menu))
    menu = result.scalars().all()
    return menu
