import sqlite3


def create_connection():
    conn = sqlite3.connect("users.db")
    return conn


def create_student_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            studentname TEXT NOT NULL,
            address TEXT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def create_class_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS class(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            classname TEXT NOT NULL)
    """
    )
    conn.commit()
    conn.close()


def create_student_class_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS studentclass (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            studentid INTEGER NOT NULL,
            classid INTEGER NOT NULL,
            FOREIGN KEY (studentid) REFERENCES student(id),
            FOREIGN KEY (classid) REFERENCES class(id)
        )
    """
    )
    conn.commit()
    conn.close()


def create_lecturer_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS lecturer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,           
            name TEXT NOT NULL,
            department TEXT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def create_course_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lectureid INTEGER NOT NULL,            
            coursename TEXT NOT NULL,
            department TEXT NULL,
            FOREIGN KEY (lectureid) REFERENCES lecturer(id)
        )
    """
    )
    conn.commit()
    conn.close()


def create_student_course_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS studentcourse (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            studentid INTEGER NOT NULL,
            courseid INTEGER NOT NULL,
            FOREIGN KEY (studentid) REFERENCES student(id),
            FOREIGN KEY (courseid) REFERENCES course(id)
        )
    """
    )
    conn.commit()
    conn.close()
