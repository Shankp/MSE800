from database import (
    create_student_table,
    create_student_class_table,
    create_lecturer_table,
    create_course_table,
    create_student_course_table,
    create_class_table
)
from services.student_service import StudentService
from services.course_service import CourseService
from services.lecturer_service import LecturerService
from services.class_service import ClassService


def menu():
    print("\n==== Student Manager ====")
    print("Inserting class , courses and lectueres to college database")

    print("\n1. Add Student")
    print("2. View All Students")
    print("3. view all Lecturers")
    print("4. View All courses")
    print("5. View All Classes")
    print("6. Exit")


def insert_initial_data():
    # insert lecturers to database
    lecturer = LecturerService()
    lecturer.add_lecturer(1, "Dr. Alice", "Computer Science")
    lecturer.add_lecturer(2, "Prof. Bob", "Computer Science")
    lecturer.add_lecturer(3, "Dr. Carol", "Computer Science")

    # insert courses to database
    course = CourseService()
    course.add_course(1, "Professional software engineering", "Computer Science", 1)
    course.add_course(2, "Quantum Computing", "Computer Science", 2)
    course.add_course(3, "Research methodalogies", "Computer Science", 3)

    # insert classes to database
    class_service = ClassService()
    class_service.add_class(1, "MSE_A")
    class_service.add_class(2, "MSE_B")

    # insert students to database
    student_service = StudentService()
    student_service.add_student(1, "John Doe", "123 Elm St", 1, 1)
    #student_service.add_student(2, "Jane Smith", "456 Oak St", 2, 2)
    #student_service.add_student(3, "Alice Johnson", "789 Pine St", 3, 1)


def main():
    create_student_table()
    create_class_table()
    create_student_class_table()
    create_lecturer_table()
    create_course_table()
    create_student_course_table()

    insert_initial_data()
    student_id = 3
    student_service = StudentService()
    lec = LecturerService()
    class_service = ClassService()
    course_service = CourseService()

    while True:
        menu()
        choice = input("\nSelect an option (1-5): ")

        if choice == "1":
            name = input("\nEnter student name: ")
            address = input("Enter student address: ")
            courseid = int(input("Enter course ID: "))
            classid = int(input("Enter class ID: "))
            student_service.add_student(student_id, name, address, courseid, classid)
            student_id += 1
        
        elif choice == "2":
            students = student_service.view_students()
            for student in students:
                print(student)
            
        elif choice == "3":
            lecs = lec.view_lecturers()
            for lec in lecs:
                print(lec)

        elif choice == "4":
            courses = course_service.view_courses()
            for course in courses:
                print(course)

        elif choice == "5":
            classes = class_service.view_classes()
            for classe in classes:
                print(classe)

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
