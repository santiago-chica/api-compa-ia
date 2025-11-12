from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from typing import Generator

URL = "sqlite:///./test.db" # probablemente mejor que vaya en un .env

engine = create_engine(
    URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# usar base para las exportaciones
class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()