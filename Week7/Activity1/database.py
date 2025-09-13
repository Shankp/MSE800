import sqlite3

def create_connection():
    conn = sqlite3.connect("app.db")
    return conn

def create_database_tables():
    create_users_table()
    create_orders_table()

def create_users_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_orders_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER NOT NULL,
            product TEXT NOT NULL,
            FOREIGN KEY (userid) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()
