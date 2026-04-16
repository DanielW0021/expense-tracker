import sqlalchemy
from sqlalchemy.orm import sessionmaker
from .models import Base

engine = sqlalchemy.create_engine('sqlite:///expenses.db')
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)