from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from src.utils.settings import settings


class Base(DeclarativeBase):
    pass

engine = create_engine(url=settings.db_connection )

LocalSession = sessionmaker(bind=engine)




def get_db ():
    Sesson = LocalSession()
    try:
        yield Sesson
    finally:
        Sesson.close()