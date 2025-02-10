from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class Base(DeclarativeBase):
    pass


def init_db(connection_string: str, engine_kwargs: dict) -> scoped_session:
    """
    Stands up all tables in the database.

    Args:
        connection_string (str): The connection string to the database.
        engine_kwargs (dict): The keyword arguments to pass to the engine (dialect-specific).

    Returns:
        A scoped session generator to use for database operations.
    """
    from src.models import item, receipt  # noqa: F401

    engine = create_engine(url=connection_string, **engine_kwargs)
    Base.metadata.create_all(engine)
    return scoped_session(sessionmaker(engine, expire_on_commit=False))
