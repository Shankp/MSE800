import sqlite3
from database import create_connection


class ClassService:
    def add_class(self, id, name):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO class (id, classname) VALUES (?, ?)", (id, name)
            )
            conn.commit()
            print("Class added successfully.")
        except sqlite3.IntegrityError:
            print("ID must be unique.")
        finally:
            conn.close()

    def view_classes(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM class")
        classes = cursor.fetchall()
        conn.close()
        return classes
