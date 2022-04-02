'''
Operator overloading in Python
    Operators in python can be overloaded using dunder methods. Dunder methods are those methods which have underscores.
    These methods are called when a given operator is used on the objects.
'''
class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        print("Lets add")
        return self.num + num2.num
    def __mul__(self,num2):
        print("Lets multiply")
        return self.num * num2.num
    # used  to set what gets displayed upon calling str(obj)
    def __str__(self):
        return f"Decimal Number: {self.num}"
    # used to set what gets displayed upon calling .__len__() or len(obj)
    def __len__(self):
        return 1

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2 
mul = n1 * n2

print(sum)
print(mul)

'''
p1 – p2 -> p1.__sub__(p2)
p1 * p2 -> p1.__mul__(p2)
p1 / p2 -> p1.__truediv__(p2)
p1 // p2 -> p1.__floordiv__(p2) the floor division // rounds the result down to the nearest whole number
'''

n = Number(9)
print(n) # __str__ method will run if we directly print n.
print(len(n))