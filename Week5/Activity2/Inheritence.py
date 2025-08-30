class Person:
    id:int
    name:str
    address:str
    age:int

class Student(Person):
    record:str

class Staff(Person):
    tax_code:str
    pay_rate:int  

class Lecturer(Staff):   
    salary:int


def main():
    student = Student()
    student.id=1 #ID is inherited from parent class Person
    student.name='test1' #name is inherited from parent class Person
    student.record ="test" #record is within the child class
    print('Student Id :' ,student.id)

    lec =  Lecturer()
    lec.name= 'lec1'
    print(' lec.name :' , lec.name)



if __name__== "__main__":
    main()

