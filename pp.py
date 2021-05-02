# OOP.

"""class Employee():
    pass

emp_1 = Employee()
emp_2 = Employee()

emp_1.name = 'Corey Fischer'
emp_2.name = 'Constructer'

print(emp_1.name)

print(emp_1)
print(emp_2)


class Employee():
    No_of_employees = 0
    Raise_salary = 1.04

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.email = name.lower().replace(' ', '') + '.gmail.com'
        Employee.No_of_employees += 1

    def fullname(self):
        return f"The age of {self.name} is {self.age} and her email is {self.email}"
    def apply_new_salary(self):
        return f"New salary of {self.name} is {self.salary * self.Raise_salary}"

    @classmethod
    def Raise_amount(cls, amount):
       cls.Raise_salary = amount

    @classmethod
    def from_string(cls, person):
        name, age, salary = person.split(',')
        return cls(name, age, salary)
        
    

emp1 = Employee('Natasha Romanoff', 38, 15000000)
emp2 = Employee('Wanda Maximoff', 30, 15000000)

emp1.Raise_amount(1.09)


print(emp1.apply_new_salary())
print(emp1.Raise_salary)
print(Employee.Raise_salary)
#print(emp1.fullname(), "while", emp2.fullname())
print(emp1.apply_new_salary())
print(emp2.apply_new_salary())

print(Employee.No_of_employees)

#for class methods

person1 ="Steve Rodgers, 40, 25000000"
person2 = "Tony Starks, 45, 50000000"
person3 = "Thor, 1500, 25000000"

#name, age, salary = person1.split(',')


#emp3 = Employee(name, age, salary)

emp3 = Employee.from_string(person1)

print(emp3.fullname())
"""

class child():
    factor = 1.09
    def __init__(self, name, school, course, allowance):
        self.name = name
        self.school = school
        self.course = course
        self.allowance = allowance
    def all_increase(self):
        return f"The allowance of {self.name} this year is {int(self.allowance * self.factor)}"

    @classmethod
    def from_string(cls, new_child):
        name, school, course, allowance = new_child.split(',')
        return cls(name, school, course, allowance)

    @classmethod
    def amount(cls, new_factor):
        cls.factor =new_factor

    @staticmethod
    def age(allow):
        if allow >= 20000:
            return "Adult."
        else:
            return "Child."



henry = child("Henry Mogere", "UoN", "Economics and Statistics", 32000)
child1 = "Kenaz Rakiro,Primary School,class 3,8000"
child2 = "Teressa Tandi,preschool,not applicable,0"

pay = henry.allowance

print(child.age(pay))


ken = child.from_string(child1)

print(ken.school)

child.amount(1.12)

print(henry.factor)
print(henry.all_increase())

