''' 
In Python, getters and setters are not the same as those in other object-oriented programming languages. 
    We use getters & setters to add validation logic around getting and setting a value.
    To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.
'''
class Employee:
    company ="Google"
    salary = 100
    salaryBonus = 20
    
    # The method name with @property decorator is called getter method.
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    #setter method
    @totalSalary.setter
    def totalSalary(self,val):
        self.salaryBonus = val - self.salary

e = Employee()
print(e.totalSalary)
'''
if e = Employee() is an object of class employee, 
we can print (e.totalSalary) top print the totalSalary or its function.
'''

e.totalSalary = 110
print(e.salary)
print(e.salaryBonus)