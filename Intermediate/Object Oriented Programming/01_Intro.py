# Solving a problem by creating objects is one of the most popular approaches in programming. 
# This is called object-oriented programming.
# This concept focuses on using reusable code. (Implements DRY principle) DRY- Don't Repeat Yourself.


class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)

## Object

'''
Object
    An object is an instantiation of a class. When class is defined, a template(info) is defined. 
    Memory is allocated only after object instantiation.
    Objects of a given class can invoke the methods available to it without revealing the implementation details to the user.    
    # Abstraction & Encapsulation
'''

# Class Attributes
# An attribute that belongs to the class rather than a particular object.

class Employee:
	company = "Google" 	        #Specific to each class
    
employee = Employee()	        #Object instantiation
employee.company
Employee.company = "YouTube"	#Changing class attribute


# Instance Attributes
# An attribute that belongs to the Instance (object)

employee.salary = 3000000 # Instance class as it is not present in class

'''
Note: Instance attributes take preference over class attributes during assignment and retrieval.
    instance.attribute1  :
        Is attribute1 present in the object?
        Is attribute1 present in class?
'''
# AttributeError: 'Employee' object has no attribute 'address' Because there is no instance or class attribute of the name address
# print(employee.address)

# Self

class SelfEmployee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is 100K")

Abhinav = SelfEmployee()
Abhinav.getSalary() # This line is converted into the below line. That's why one positional argument was given here in the name of Abhinav
# SelfEmployee.getSalary(Abhinav)

'''
‘self’ parameter
    self refers to the instance of the class.
    It is automatically passed with a function call from an object.
'''
