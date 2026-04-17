import flet as ft
from core.services import FinanceService

class AppLayout(ft.Row):
    def __init__(self, finance_service: FinanceService):
        super().__init__()
        self.expand = True
        self.service = finance_service

        self.rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=200,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icons.DASHBOARD_OUTLINED,
                    selected_icon=ft.Icons.DASHBOARD,
                    label="Dashboard",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.ATTACH_MONEY_OUTLINED,
                    selected_icon=ft.Icons.ATTACH_MONEY,
                    label="Spent",
                ),
            ],
            on_change=self.change_page
        )

        self.content_area = ft.Column(
            [ft.Text("Welcome to Expense Tracker!")], 
            expand=True,
            alignment=ft.MainAxisAlignment.START
        )

        self.controls = [
            self.rail,
            ft.VerticalDivider(width=1),
            self.content_area,
        ]

    def _build_dashboard_view(self):
        import datetime
        now = datetime.date.today()
        spent, budget = self.service.get_monthly_data(now.month, now.year)
        
        return ft.Column([
            ft.Text("Podsumowanie miesiąca", size=30, weight="bold"),
            ft.Row([
                ft.Container(
                    content=ft.Text(f"Wydano: {spent} zł", size=20),
                    bgcolor="red", padding=20, border_radius=10
                ),
                ft.Container(
                    content=ft.Text(f"Budżet: {budget} zł", size=20),
                    bgcolor="green", padding=20, border_radius=10
                ),
            ])
        ], expand=True)
        
    def _build_expenses_view(self):
        all_expenses = self.service.expense_repo.get_all()
        
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Date")),
                ft.DataColumn(ft.Text("Category")),
                ft.DataColumn(ft.Text("Amount")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(e.date))),
                        ft.DataCell(ft.Text(e.category.name if e.category else "Other")),
                        ft.DataCell(ft.Text(f"{e.amount} zł")),
                    ]
                ) for e in all_expenses
            ]
        )
        
        return ft.Column([
            ft.Text("History of Expenses", size=25, weight="bold"),
            ft.Divider(),
            table
        ], scroll=ft.ScrollMode.AUTO)
        
    def change_page(self, e):
        index = e.control.selected_index
        self.content_area.controls.clear()
        
        if index == 0:
            self.content_area.controls.append(self._build_dashboard_view())
        elif index == 1:
            self.content_area.controls.append(self._build_expenses_view())
        
        self.update()