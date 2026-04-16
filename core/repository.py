from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from core.models import Expense, Category, Budget

class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session
        
    def add(self, name: str, icon: str, color: str):
        category = Category(name=name, icon=icon, color=color)
        self.session.add(category)
        self.session.commit()
        self.session.refresh(category)
        return category

    def get_all(self):
        return self.session.execute(select(Category)).scalars().all()
    
    def get_by_id(self, cat_id: int):
        return self.session.get(Category, cat_id)
    
class ExpenseRepository:
    def __init__(self, session: Session):
        self.session = session
        
    def add(self, amount: float, description: str, category_id: int, date):
        expense = Expense(amount=amount, description=description, category_id=category_id, date=date)
        self.session.add(expense)
        self.session.commit()
        self.session.refresh(expense)
        return expense    
    
    def get_all(self):
        return self.session.execute(select(Expense).options(joinedload(Expense.category))).scalars().all()
    
    def get_by_range(self, start_date, end_date):
        return self.session.execute(
            select(Expense).where(Expense.date.between(start_date, end_date)).options(joinedload(Expense.category))
        ).scalars().all()
        
class BudgetRepository:
    def __init__(self, session: Session):
        self.session = session
        
    def add(self, category_id: int, limit: float, month: int, year: int):
        budget = Budget(category_id=category_id, limit=limit, month=month, year=year)
        self.session.add(budget)
        self.session.commit()
        self.session.refresh(budget)
        return budget    
        
    def get_budget_for_month(self, month: int, year: int):
        return self.session.execute(
            select(Budget).where(Budget.month == month, Budget.year == year).options(joinedload(Budget.category))
        ).scalars().all()       