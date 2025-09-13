import sqlite3

from db_connection_singleton import DatabaseConnectionSingleton
 
class UserService:
    def get_user(self, user_id):
        conn = sqlite3.connect('app.db')  # New connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result
    
    def insert_user(self, user_id, name):
        conn = sqlite3.connect('app.db')  # New connection
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user_id, name))
        conn.commit()
        conn.close()
 
class OrderService:
    def get_orders(self, user_id):
        conn = sqlite3.connect('app.db')  # Another new connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE userid = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result
    
    def insert_order(self, order_id, user_id, product):
        conn = sqlite3.connect('app.db')  # Another new connection
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (id, userid, product) VALUES (?, ?, ?)", (order_id, user_id, product))
        conn.commit()
        conn.close()

#service that uses singleton pattern for db connection
class UserService_singleton:
    def __init__(self):
        self.db = DatabaseConnectionSingleton().get_connection()  # Single connection
    
    def get_user(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        return result
    
    def insert_user(self, user_id, name):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user_id, name))
        self.db.commit()

class OrderService_singleton:
    def __init__(self):
        self.db = DatabaseConnectionSingleton().get_connection()  # Single connection

    def get_orders(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM orders WHERE userid = ?", (user_id,))
        result = cursor.fetchall()
        return result

    def insert_order(self, order_id, user_id, product):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO orders (id, userid, product) VALUES (?, ?, ?)", (order_id, user_id, product))
        self.db.commit()
        cursor.execute("SELECT * FROM orders WHERE userid = ?", (user_id,))
        result = cursor.fetchall()        
        return result
    
    def insert_order(self, order_id, user_id, product):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO orders (id, userid, product) VALUES (?, ?, ?)", (order_id, user_id, product))
        self.db.commit()