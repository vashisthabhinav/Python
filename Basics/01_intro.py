# Python
'''Multiline
 comment
'''
import os
print("Hello World")
print('''If the string is larger than one line (paragraph),
We would use this kind of notation to print the files.''')
print(os.listdir())#Using os import

#Variables and Datatypes
'''Variable – Container to store a value

Keywords – Reserved words in Python

Identifiers – class/function/variable name

Data Types:
Primarily there are the following data types in Python:

Integers
Floating point numbers
Strings
Booleans
None'''
a = "Abhinav Vashisth"
b = 336
c = 34.98
d = True
e = None
# Printing the variables
print(a)
print(b) 
print(c)
print(d) 
print(e)

# Printing the type of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

'''Rules for defining a variable name: (Also applicable to other identifiers)

A variable name can contain alphabets, digits, and underscore.
A variable name can only start with an alphabet and underscore.
A variable can’t start with a digit.
No white space is allowed to be used inside a variable name.'''

# Operators In Python
'''Operators in Python
The following are some common operators in Python:

- Arithmetic Operators (+, -, *, /, etc.)
- Assignment Operators (=, +=, -=, etc.)
- Comparison Operators (==, >=, <=, >, <, !=, etc.)
- Logical Operators (and, or, not)'''

# Assignment Operators
x = 34
x-= 12
x*= 21
x/= 7
print("The value of x is: ",x) 

# Comparison Operators
y = (4>=7)
print(y)
y = (8>7)
print(y)
print(12==12)
print(12!=21)

# Logical Operators
b1 = True
b2 = False
print("The value of b1 and b2 is: ", (b1 and b2))
print("The value of b1 or b2 is: ", (b1 or b2))
print("The value of not b2 is: ", (not b2))

#Typecasting
'''type() function and Typecasting

type function is used to find the data type of a given variable in Python.
A number can be converted into a string and vice versa (if possible)

There are many functions to convert one data type into another.
'''
a1 = 31
str(a1)           # "31" Integer to string conversion
print(a1)
print(type(a1))

a2 = int("32")       # 32 String to int conversion
print(a2)
print(type(a2))

a3 = float(32)       #32.0 Integer to float conversion
print(a3)
print(type(a3))

# Input Function
'''input() function

This function allows the user to take input from the keyboard as a string.
Note: The output of the input function is always a string even if the number is entered by the user.

Suppose if a user enters 34, then this 34 will automatically convert to “34” string literal.'''
m = input("Enter your name: ")
print(m)
n = input("Enter a number: ")
n = int(n)
print(n) # Converting n to integer(if possible)
print(type(n))

# Average
m1 = input("Enter m1: ")
n1 = input("Enter m2: ")
m1 = int(m1)
n1 = int(n1)
avg = (m1+n1)/2
print(avg)
