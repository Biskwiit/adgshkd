class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")


student1 = Student("Jasmine", 22, "Tourism Management")
student2 = Student("Bob", 22, "Information Technology")
student3 = Student("Potpot", 22, "Business")


student1.introduce()
student2.introduce()
student3.introduce()