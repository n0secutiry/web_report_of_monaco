import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.app import app
from app.database import database
from app.database.models import Base

TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost/test_sql_task"

test_engine = create_engine(TEST_DATABASE_URL, echo=False)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="function")
def init_database():
    Base.metadata.create_all(bind=test_engine)

    original_session_maker = database.SessionLocal
    database.SessionLocal = TestingSessionLocal

    session = TestingSessionLocal()
    yield session

    session.close()
    database.SessionLocal = original_session_maker
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="function")
def test_client(init_database):
    with app.test_client() as client:
        yield client
