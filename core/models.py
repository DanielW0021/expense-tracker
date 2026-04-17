import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedAsDataclass, relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase, MappedAsDataclass):
    pass

class Category(Base):
    __tablename__ = "categories"
    name: Mapped[str] = mapped_column()
    icon: Mapped[str] = mapped_column()
    color: Mapped[str] = mapped_column()
    id: Mapped[int] = mapped_column(primary_key=True, init=False)

class Expense(Base):
    __tablename__ = "expenses"
    amount: Mapped[float] = mapped_column()
    description: Mapped[str] = mapped_column()
    category: Mapped[Category] = relationship(init=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    date: Mapped[datetime.date] = mapped_column()
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    created_at: Mapped[datetime.datetime] = mapped_column(default_factory=datetime.datetime.now)
    

class Budget(Base):
    __tablename__ = "budgets"
    category: Mapped[Category] = relationship(init=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    limit: Mapped[float] = mapped_column()
    month: Mapped[int] = mapped_column()
    year: Mapped[int] = mapped_column()
    id: Mapped[int] = mapped_column(primary_key=True, init=False)