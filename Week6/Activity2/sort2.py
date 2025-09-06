if __name__ == "__main__":
    students = [
        {'name': "John", 'grade': "A", 'age': 20},
        {'name': "Jane", 'grade': "B", 'age': 21},
        {'name': "Joss", 'grade': "A+", 'age': 19},
        {'name': "Jack", 'grade': "A-", 'age': 16},
        {'name': "Dave", 'grade': "C", 'age': 25},
    ]

    sorted_students = sorted(students, key = lambda x : ( x['age']))
    print(sorted_students)