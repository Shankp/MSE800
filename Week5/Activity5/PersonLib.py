class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def greet(self):
        print("Greetings1 :", self.name)