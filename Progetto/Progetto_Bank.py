from datetime import datetime
import sqlite3
import customtkinter as ctk
from dataclasses import dataclass

@dataclass #è un modulo che serve creare classi che sono principalmente utilizzate per immagazzinare dati (spero sia così)
class Transaction:
    amount: float
    category: str
    description: str
    date: datetime = datetime.now()
    type: str = "expense"  # expense/income

class BudgetTracker:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.setup_database()
        
    def setup_database(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                amount REAL,
                category TEXT,
                description TEXT,
                date TEXT,
                type TEXT
            )
        """)
        self.conn.commit()

    def add_transaction(self, transaction: Transaction):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (amount, category, description, date, type)
            VALUES (?, ?, ?, ?, ?)
        """, (
            transaction.amount,
            transaction.category,
            transaction.description,
            transaction.date.isoformat(),
            transaction.type
        ))
        self.conn.commit()

    def get_transactions(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        return cursor.fetchall()

    def get_balance(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
        income = cursor.fetchone()[0] or 0
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
        expense = cursor.fetchone()[0] or 0
        return income - expense

class BudgetApp(ctk.CTk):
    def __init__(self, budget_tracker: BudgetTracker):
        super().__init__()
        self.budget_tracker = budget_tracker
        self.title("Budget Tracker")
        self.geometry("400x400")

        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Amount")
        self.amount_entry.pack(pady=10)

        self.category_entry = ctk.CTkEntry(self, placeholder_text="Category")
        self.category_entry.pack(pady=10)

        self.description_entry = ctk.CTkEntry(self, placeholder_text="Description")
        self.description_entry.pack(pady=10)

        self.type_var = ctk.StringVar(value="expense")
        self.expense_radio = ctk.CTkRadioButton(self, text="Expense", variable=self.type_var, value="expense")
        self.expense_radio.pack(pady=5)
        self.income_radio = ctk.CTkRadioButton(self, text="Income", variable=self.type_var, value="income")
        self.income_radio.pack(pady=5)

        self.add_button = ctk.CTkButton(self, text="Add Transaction", command=self.add_transaction)
        self.add_button.pack(pady=10)

        self.balance_label = ctk.CTkLabel(self, text="Balance: $0.00")
        self.balance_label.pack(pady=10)

        self.update_balance()

    def add_transaction(self):
        amount = float(self.amount_entry.get())
        category = self.category_entry.get()
        description = self.description_entry.get()
        type_ = self.type_var.get()
        transaction = Transaction(amount=amount, category=category, description=description, type=type_)
        self.budget_tracker.add_transaction(transaction)
        self.update_balance()

    def update_balance(self):
        balance = self.budget_tracker.get_balance()
        self.balance_label.configure(text=f"Balance: ${balance:.2f}")

if __name__ == "__main__":
    db_path = "budget.db"
    budget_tracker = BudgetTracker(db_path)
    app = BudgetApp(budget_tracker)
    app.mainloop()