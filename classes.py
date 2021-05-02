class Student:
    def print_hello(self):
        print("Hello world")


a = Student()
b = Student()

# a.print_hello()
# b.print_hello()

a.name = "Student One"
a.GPA = 3.8
a.course = "ETE"

b.name = "Two"
# print(a.GPA)
# print(b.GPA)
"""
class Student():
    def __init__(self, name, gpa=3.0, course="ETE"):
        self.name = name
        self.gpa = gpa
        self.course = course
    def print_hello(self):
        print(self.name)
    def modify_name(self, x):
        self.name = x
    def __call__(self):
        print(f"Object {self.name} initialized")

st1 = Student("Student")
st1()
st1.modify_name("Graduate")
print(st1.name)
# print()
st1.age = 43

"""
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def __call__(self):
        return f"Name : {self.name} Id : {self.id}"
        # return "Name : {} Id : {}".format(self.name, self.id)

class Manager(Employee):
    def __init__(self, name, id, meetings):
        super().__init__(name, id)
        self.name = name
        self.id = id
        self.meetings = meetings
    def __call__(self):
        print("Manager employed")

manager = Manager("Management Officer" , 0000, 5)
manager()

# emp = Employee("Emp", "1111")
# print(emp())