from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_URL = "sqlite:///./task.db"

engine = create_engine(
    SQLALCHEMY_URL,
    connect_args={"check_same_thread": False} #only for sqlite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
#
#
# engine = create_async_engine(
#     "sqlite+aiosqlite:///task.db"
# )
#
# new_session = async_sessionmaker(engine, expire_on_commit=False)
#
# class Base(DeclarativeBase):
#     pass
#
#
# class TaskORM(Base):
#     __tablename__ = "tasks"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     description: Mapped[str | None] = None
#
#
# async def create_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
#
# async def delete_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
