from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()
from sqlalchemy.pool import NullPool

from app.config import settings

if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {}


engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

#async_session_maker = sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)
async_session_maker = async_sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)

class Base(DeclarativeBase):
    pass

