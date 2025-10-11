from expense_processor import ExpenseApp
from user import User
from db import db

if __name__ == "__main__":
    app = ExpenseApp(db)
    # register a user
    email = input("Enter your email: ")
    username = input("Enter your username: ")
    user = User(username=username, email=email)
    user_id = user.user_register()

    # add some expenses
    foodExpense = int(input("Enter your food expense: "))
    app.add_expense(user_id=user_id, amount=foodExpense, category="Food")
    rentExpense = int(input("Enter your rent expense: "))
    app.add_expense(user_id=user_id, amount=rentExpense, category="Rent")
    utilitiesExpense = int(input("Enter your utilities expense: "))
    app.add_expense(user_id=user_id, amount=utilitiesExpense, category="Utilities")

    # retrieve and display expenses
    total = app.get_expenses(user_id=user_id)
    print(f"Total expenses for user {username}: ${total}")