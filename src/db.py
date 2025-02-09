from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session




class Base(DeclarativeBase):
    pass


def init_db(connection_string: str, engine_kwargs: dict) -> scoped_session:
    engine = create_engine(url=connection_string, **engine_kwargs)
    Base.metadata.create_all(engine)
    return scoped_session(sessionmaker(engine, expire_on_commit=False))
