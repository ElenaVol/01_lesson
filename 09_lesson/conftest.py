import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base

# ЗАМЕНИТЕ ДАННЫЕ НА СВОИ
DB_URL = "postgresql://postgres:1406@localhost:5432/QA"

@pytest.fixture(scope='session')
def db_engine():
    """Движок для подключения к БД. Создается один раз на все тесты."""
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)  
    yield engine
  
@pytest.fixture(scope='function')
def db_session(db_engine):
    """Сессия для каждого теста. Транзакция откатывается после теста."""
    connection = db_engine.connect()
    transaction = connection.begin()
    Session = scoped_session(sessionmaker(bind=connection))
    session = Session()

    yield session

    session.close()
    transaction.rollback()  
    connection.close()