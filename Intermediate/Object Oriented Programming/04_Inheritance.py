# Inheritance is a way of creating a new class from an existing class.
'''
We can use the methods and attributes of Employee in Programmer object.
Also, we can overwrite or add new attributes and methods in the Programmer class.
'''
class Employee:
    company = "Google"
    def showDetails(self):
        print("This is an employee.")

class Programmer(Employee):
    language = "Python"
    company = "Youtube"
    def getLanguage(self):
        print(f"The language is {self.language} ")
    def showDetails(self):
        print("This is an programmer.")

e = Employee()
e.showDetails()
p =  Programmer()
p.showDetails()

# Type of Inheritance
'''
Type of Inheritance-
    Single inheritance
    Multiple inheritance
    Multilevel inheritance
'''

# Single Inheritance
'''
Single inheritance occurs when a child class inherits only a single parent class.
Base -> Derived
The above example was Single Inheritance.
'''

# Multiple Inheritance
'''
Multiple inheritances occurs when the child class inherits from more than one parent class.
'''
class Employee2:
    company = "Visa"
    eCode  = 120

class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradeLevel(self):
        self.level = self.level+1

class Programmer2(Employee2,Freelancer):
    name = "XYZ"
    
p = Programmer2()
print(p.level)
p.upgradeLevel()
print(p.level)

print(p.company)#This line will print visa because Employee2 is written before Freelancer in --> class Programmer2(Employee2,Freelancer):

# Multilevel Inheritance
'''When a child class becomes a parent for another child class.'''

class Parent:
    country = "India"
    city = "Hamirpur"

    def getSalary(self):
        print("The salary of Parent is..")

class Child(Parent):
    city = "Shimla"

    def getSalary(self):
        print("The salary of Child is..")
 
class GrandChild(Child):
    city = "Bangaluru"

    def getSalary(self):
        print("The salary of GrandChild is..")
    
     
p = Parent()
p.getSalary()
c = Child()
c.getSalary()
gc = GrandChild()
gc.getSalary()
print(gc.city)
print(gc.country)