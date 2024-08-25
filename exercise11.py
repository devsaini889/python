# a program to understand the inheritance concept of Oop

class Docter:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("role = ",self.role)
        print("department = ",self.dept)
        print("salary = ",self.salary)

class Teacher(Docter):
    def __init__(self, name, age,):
        self.name = name
        self.age=age

        super().__init__("Teacher", "school", "40k")


a1 = Teacher("Rajesh" , 25) 
a1.show_details()
