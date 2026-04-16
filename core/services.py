from .repository import ExpenseRepository, CategoryRepository, BudgetRepository
import calendar, datetime

class FinanceService:
    def __init__(self, expense_repo: ExpenseRepository, 
                 category_repo: CategoryRepository, 
                 budget_repo: BudgetRepository):
        self.expense_repo = expense_repo
        self.category_repo = category_repo
        self.budget_repo = budget_repo
        
    def _get_monthly_expenses(self, month, year):
        date = calendar.monthrange(year, month)[1]
        return self.expense_repo.get_by_range(datetime.date(year, month, 1), datetime.date(year, month, date))
        
    def get_monthly_data(self, month: int, year: int):
        expenses = self._get_monthly_expenses(month, year)
        budgets = self.budget_repo.get_budget_for_month(month, year)
        return sum(e.amount for e in expenses), sum(b.limit for b in budgets)
    
    def get_category_summary(self, month: int, year: int):
        expenses = self._get_monthly_expenses(month, year)
        summary = {}
        for expense in expenses:
            cat_name = expense.category.name
            summary[cat_name] = summary.get(cat_name, 0) + expense.amount
        return summary