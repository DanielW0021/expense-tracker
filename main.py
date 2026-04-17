import flet as ft
from core.database import SessionLocal, init_db
from core.repository import ExpenseRepository, CategoryRepository, BudgetRepository
from core.services import FinanceService
from ui.app import AppLayout

def main(page: ft.Page):
    page.title = "Expense Tracker"
    page.window_width = 1000
    page.window_height = 700

    init_db()
    db = SessionLocal()
    category_repo = CategoryRepository(db)
    expense_repo = ExpenseRepository(db)
    budget_repo = BudgetRepository(db)

    finance_service = FinanceService(expense_repo, category_repo, budget_repo)

    app_layout = AppLayout(finance_service)
    page.add(app_layout)
    
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)