from sqlalchemy import create_engine, Column, Integer, Float, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class CategoryORM(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)
    icon = Column(String)
    
class ExpenseORM(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    date = Column(Date)
    created_at = Column(DateTime)
    
class BudgetORM(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer)
    limit = Column(Float)
    month = Column(Integer)
    year = Column(Integer)
    
engine = create_engine('sqlite:///expenses.db')
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)            
