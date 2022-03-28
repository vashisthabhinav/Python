# Super() method
'''
Super method is used to access the methods of a superclass in the derived class.
'''

class Parent:
    country = "India"
    city = "Hamirpur"

    def __init__(self) -> None:
        print("Parent")

    def getSalary(self):
        print("The salary of Parent is..")

class Child(Parent):
    city = "Shimla"

    def __init__(self) -> None:
        super().__init__()
        print("Child")

    def getSalary(self):
        super().getSalary()
        print("The salary of Child is..")
 
class GrandChild(Child):
    city = "Bangaluru"

    def __init__(self) -> None:
        super().__init__()
        print("GrandChild")

    def getSalary(self):
        super().getSalary()
        print("The salary of GrandChild is..")
    
gc = GrandChild()
gc.getSalary()
# print(gc.city)
# print(gc.country)