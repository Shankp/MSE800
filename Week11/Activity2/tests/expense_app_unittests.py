import pytest
import unittest
from db import db
from expense_processor import ExpenseApp
from user import User
from unittest.mock import patch


class TestExpenseApp(unittest.TestCase):
 
    def test_total_expenses(self):
        # Setup
        app = ExpenseApp(db)
        user = User(username="testuser", email="test@example.com")
        mock_user_register = patch.object(User, 'user_register', return_value=user.id) #todo: Mock user_register method
        mock_user_register.start()
        app.add_expense(user_id=user.id, amount=50, category="Food")
        app.add_expense(user_id=user.id, amount=100, category="Rent")   
        app.add_expense(user_id=user.id, amount=30, category="Utilities")

        # Test
        total = app.get_expenses(user_id=user.id)
        self.assertEqual(total, 180)