from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from typing import Generator

from config.config import settings

engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

class Base(DeclarativeBase):
    pass

def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session
