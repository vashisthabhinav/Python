class Programmer:
    company = "Microsoft"
    def __init__(self,name,product) :
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the programmer is {self.name} and the product is {self.product}")

Abhinav = Programmer("Abhinav", "Skype")
Chirag = Programmer("Chirag", "MS")
Abhinav.getInfo()

class Calculator:
    def __init__(self,number) -> None:
        self.number = number
    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    def squareRoot(self):
        print(f"The squareroot of {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")

a = Calculator(8100)
a.square()
a.squareRoot()
a.cube() 
