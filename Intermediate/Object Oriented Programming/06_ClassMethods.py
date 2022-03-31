# Class methods
'''
A class method is a method which is bound to the class and not the object of the class.
    @classmethod decorator is used to create a class method.
    Also __class__ can also be used.
'''
class Employee:
    company ="Google"
    salary = 100;
    location = "Delhi"
    # def changeSalary(self,sal): #Method-1
    #     self.__class__.salary = sal
    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
