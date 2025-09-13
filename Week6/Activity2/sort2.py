if __name__ == "__main__":
    students = [
        {"name": "John", "grade": "A", "age": 20},
        {"name": "Jane", "grade": "B", "age": 21},
        {"name": "Joss", "grade": "A+", "age": 19},
        {"name": "Jack", "grade": "A-", "age": 16},
        {"name": "Dave", "grade": "C", "age": 25},
    ]

    # for each item in the list, value in the  'age' dict key is used for sorting
    sorted_students = sorted(
        students, key=lambda x: (x["age"])
    )  
    print(sorted_students)

    # Reverse sorting based on age
    desc_sorted_students = sorted(students, key=lambda x: (x["age"]), reverse=True)
    print(desc_sorted_students)
