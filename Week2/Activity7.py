class Employee:
    def __init__(self, name, age, salary, jobTitle):
        self.name = name
        self.age = age
        self.salary = salary
        self.jobTitle = jobTitle

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary} , Job Title: {self.jobTitle}"


class EmployeeManager:
    def __init__(self):
        self.employeeList = {}

    def insert_employee(self, id, name,age,  salary, jobTitle):
        self.employeeList[id] = (Employee(name,age, salary, jobTitle))
        return

    def display_info(self, id):
        if not id in self.employeeList:
            return self.employeeList.values()
        return self.employeeList[id].display_details()

    def give_raise(self, id, salaryRaise):
        if not id in self.employeeList:
            return None

        employee = self.employeeList[id]
        employee.salary += salaryRaise
        self.employeeList[id] = employee
        return self.employeeList[id]       
    

def main():
    employeeManager = EmployeeManager()
    employee_number = 1
    #feed initial data
    employeeManager.insert_employee(employee_number, "Alice",30, 50000, "Software Engineer")
    employee_number += 1
    employeeManager.insert_employee(employee_number, "Bob",35, 60000, "Data Scientist")

    print("\nCommands:")
    print("Type 'display' to show all employees or 'exit' to quit.") 
    print("Type 'update' to give a raise to an employee.") 
    print("Type 'insert' to give a add to an employee.") 
   
    user_command = ""
    while(user_command != "exit"):
        user_command = input("\nEnter command: ")

        if(user_command == "exit"):
            print("\nExiting the program.")
            break

        elif user_command == "display":
            print("\nAll Employees:")
            for emp in employeeManager.display_info(0):
                print(emp.display_details())

        elif user_command == "insert":
            name = input("\nEnter employee name: ")
            age = int(input("Enter employee age: "))
            salary = float(input("Enter employee salary: "))
            jobTitle = input("Enter employee job title: ")
            employee_number += 1
            employeeManager.insert_employee(employee_number, name, age, salary, jobTitle)
            print("Employee added successfully.")

        elif user_command == "update":
            emp_id = int(input("\nEnter employee ID to give a raise: "))
            raise_amount = float(input("Enter raise amount: "))
            updated_employee = employeeManager.give_raise(emp_id, raise_amount)
            if updated_employee:
                print(f"Updated Employee Details: {employeeManager.display_info(emp_id)}")
            else:
                print("Employee not found.")

        else:
            print("Invalid command. Please enter 'display' or 'exit'.")       

if __name__ == "__main__":
    main()
