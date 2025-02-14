class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary raised by ₱{amount}. New salary is ₱{self.salary}.")
    
    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ₱{self.salary}")
        print("-" * 20)

employee1 = Employee("Potie Aragon", "Entrepreneur", 500000)

employee1.display_employee()

employee1.give_raise(100000)
employee1.display_employee()