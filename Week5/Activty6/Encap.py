class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # protected property

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self._age = age  # protected property
        self.__grade = "A"  # private property, can only accss through accessor(method)

    def get_grade(self):
        return self.__grade

    def get_age(self):
        return self.age


class PriamaryStudent(Student):
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.name = name
        self._age = age  # protected property
        self.__height = height  #__heigh private property, can only accss through accessor(method)


    def get_heigh(self):
        return self.__height


def main():
    print("**Student Info") 
    student = Student("John", 25)
    print("name :", student.name)  # student name is accessible as its public
    print("age :", student._age)  # student age is accessible as its protected
    print("grade :", student.get_grade())


    print("\n**Primary Student Info")
    LitStudent = PriamaryStudent("Jenny",10, 100)
    print("name :", LitStudent.name)  # PriamaryStudent name is accessible as its public
    print("height :", LitStudent.get_heigh())  # student height can access through accessor
    #print("height :", LitStudent.__height) #height cant be accessed , as its private

    try:
        print(
            "age :", student.__grade
        )  # student grade is not accessible as its private. need to access through accessor
    except:
        print("student.__grade is private variable. can access directly")


if __name__ == "__main__":
    main()
