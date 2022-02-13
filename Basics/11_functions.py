# Function
'''
A function is a group of statements performing a specific task.
A function can be reused by the programmer in a given program any number of times.
Function call-
    Whenever we want to call a function, we put the name of the function followed by parenthesis.
 
'''
def percent(marks):
    return (sum(marks)*100)/400
    
marks = [45,56,78,97]
percentage = percent(marks)
print(percentage)
'''
There are two types of functions in Python:
    Built-in functions #Already present in Python
    User-defined functions #Defined by the user
There are two types of functions in Python:
    Built-in functions #Already present in Python
    User-defined functions #Defined by the user
Default Parameter Value
    We can have a value as the default argument in a function.
    If we specify num1 = 0, num2=0 in the line containing def, this value is used when no argument is passed.
'''
def sum(num1=0,num2=0):
    return num1+num2
print(sum(23,43))
print(sum())

print("No new Line",end = "")
# Iterative approach for factorial
def factorial(n):
    product = 1
    for i in range(n):
        product = product*(i+1) #i is 0, so to start it from 1, i+1 is used.
    return product

print(factorial(7))