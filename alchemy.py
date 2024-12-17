from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Определяем URL PostgreSQL
postgresql_url = 'postgresql://postgres:1111@localhost:5432/project'

# Создаём движок
engine = create_engine(postgresql_url)

# Устанавливаем соединение
connection = engine.connect()

session = Session(engine)