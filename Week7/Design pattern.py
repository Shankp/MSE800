import sqlite3


# The design pattern used here is the Factory Method pattern.
# DBConnectionFactory provides a static method to create and return database connections.
class DBConnectionFactory:
    @staticmethod
    def get_connection():
        return sqlite3.connect("app.db")


class UserService:
    def get_user(self, user_id):
        conn = DBConnectionFactory.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result



class OrderService:
    def get_orders(self, user_id):
        conn = DBConnectionFactory.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result
