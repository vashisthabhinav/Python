# Tuples--> Creating a tuple using ()

'''
Tuples in Python:
A tuple is an immutable (can’t change or modified) data type in Python.
Once defined, tuple elements can’t be manipulated or altered.
'''
t = (1,2,3,4,5)
print(t)
# Printing the elements of a tuple
print(t[0])

# We cannot update the values of a tuple
# t[0] = 34 #'tuple' object does not support item assignment   
# print(t[0]) 


t1 = () #Empty tuple
print(t1)

t2 = (1) #Wrong way to declare a tuple with single element as it will behave as a number instead of tuple
t3 = (1,) # Tuple with single element

'''
Tuple methods:

Consider the following tuple,

a = (1, 7, 2)
count(1) – It will return the number of times 1 occurs in a.
index(1) – It will return the index of the first occurrence of 1 in a.
'''

a = (1,2,4,1,5,1,3,4,6,8,1,8)
print(a.count(1))

print(a.index(8))


