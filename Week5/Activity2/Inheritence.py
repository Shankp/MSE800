class Person:
    id:int
    name:str
    address:str
    age:int

class Student(Person):
    record:str

class Lecturer(Person):
    tax_code:str
    salary:int


class Staff(Person):
    tax_code:str
    pay_rate:int   


def main():
    student = Student()
    student.id=1 #ID is inherited from parent class Person
    student.name='test1' #name is inherited from parent class Person
    student.record ="test" #record is is within the child class
    print('Student Id :' ,student.id)

if __name__== "__main__":
    main()

