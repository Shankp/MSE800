import sqlite3
from database import create_connection

class CourseService:
    def add_course(self,id, coursename, department, lectureid):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO course (id, coursename, department, lectureid) VALUES (?, ?, ?, ?)",
                (id, coursename, department, lectureid),
            )
            conn.commit()
            print("Course added successfully.")
        except sqlite3.IntegrityError:
            print("ID must be unique.")
        finally:
            conn.close()

    def view_courses(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course")
        courses = cursor.fetchall()
        conn.close()
        return courses