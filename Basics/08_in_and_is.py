# in and is keyword
a = None
if(a is None):
    print("Yes")#This value is printed as 'a' and None are pointing to the same value
else:
    print("No")

# Python 'is' keyword

'''
The is keyword is used to test if two variables refer to the same object.

The test returns True if the two objects are the same object.

The test returns False if they are not the same object, even if the two objects are 100% equal.

Use the == operator to test if two variables are equal.
'''

# Python 'in' keyword

'''
The in keyword has two purposes:

The in keyword is used to check if a value is present in a sequence (list, range, string etc.).
'''

b = [45,23,6]
print(45 in b)
print(12 in b)