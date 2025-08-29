from PersonLib import Person

class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        #Person.__init__(name, address, age)
        self.student_id = student_id

    def greet(self):
        print("Greetings :", self.name)

def main():
    student = Student("John","test","15",123)
    student.greet()

if __name__== "__main__":
    main()



