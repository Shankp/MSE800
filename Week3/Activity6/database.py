import sqlite3


def create_connection():
    conn = sqlite3.connect("users.db")
    return conn


def create_database_tables():
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

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS class(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            classname TEXT NOT NULL)
    """
    )

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

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS lecturer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,           
            name TEXT NOT NULL,
            department TEXT NULL
        )
    """
    )

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
