import sqlite3
from database import create_connection


class StudentService:
    def __init__(self):
        pass

    def add_student(self, id, name, address, courseid, classid):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO student (id, studentname, address) VALUES (?, ?, ?)",
                (id, name, address),
            )
            cursor.execute(
                "INSERT INTO studentclass (studentid, classid) VALUES (?, ?)",
                (id, classid),
            )
            cursor.execute(
                "INSERT INTO studentcourse (studentid, courseid) VALUES (?, ?)",
                (id, courseid),
            )
            conn.commit()
            print(" Student added successfully.")
        except sqlite3.IntegrityError:
            print(" ID must be unique.")
        finally:
            conn.close()

    def view_students(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        students = cursor.fetchall()
        conn.close()
        return students
