class Person:
    def __init__(self, list):
        self.list = list


    def update_age(self, years):
        self.list[1] += years

    def display_details(self):
        return f"Name: {self.list[0]}, Age: {self.list[1]}, Address: {self.list[2]}"
    
def main():
    personal_details = []
    name = input("Enter your name: ")
    personal_details.append(name)
    age = int(input("Enter your age: "))
    personal_details.append(age)
    address = input("Enter your address: ")
    personal_details.append(address)

    personal_details = Person(personal_details)
    print("\nPersonal Details:")
    print(personal_details.display_details())

    years_to_add = int(input("\nHow many years would you like to add to your current age? "))
    personal_details.update_age(years_to_add)

    print("\nUpdated Personal Details:")
    print(personal_details.display_details())

if __name__ == "__main__":
    main()