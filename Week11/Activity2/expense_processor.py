from datetime import datetime, timezone
from db import db


class ExpenseApp:
    def __init__(self, db):
        self.db = db

    def add_expense(self, user_id, amount, category):
        expense = {
            "user_id": user_id,
            "amount": amount,
            "category": category,
            "timestamp": datetime.now(timezone.utc),
        }
        db.expenses.insert_one(expense)

    def get_expenses(self, user_id):
        rent_expense = self.get_expenses_by_category(user_id, "Rent")
        food_expense = self.get_expenses_by_category(user_id, "Food")
        utilities_expense = self.get_expenses_by_category(user_id, "Utilities")
        total = rent_expense + food_expense + utilities_expense
        return total
    
    def get_expenses_by_category(self, user_id, category):
        expenses = db.expenses.find({"user_id": user_id, "category": category})
        total = sum(expense["amount"] for expense in expenses)
        return total
