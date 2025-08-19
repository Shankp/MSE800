import sqlite3
from database import create_connection

class LecturerService:
    def add_lecturer(self,id, lecturer_name, department):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO lecturer (id, name, department) VALUES (?, ?, ?)",
                (id, lecturer_name, department),
            )
            conn.commit()
            print(" lecturer added successfully.")
        except sqlite3.IntegrityError:
            print(" ID must be unique.")
        finally:
            conn.close()

    def view_lecturers(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lecturer")
        lecturers = cursor.fetchall()
        conn.close()
        return lecturers
