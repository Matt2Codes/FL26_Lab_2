from typing import Generator
from sqlmodel import SQLModel, Session, create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# check_same_thread=False is required for SQLite with FastAPI multi-threading
engine = create_engine(sqlite_url, echo=False, connect_args={"check_same_thread": False})


def init_db() -> None:
    """Create tables based on SQLModel metadata."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """FastAPI dependency yielding a managed database session."""
    with Session(engine) as session:
        yield session
