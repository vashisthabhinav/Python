# Lists
# Python Lists are containers to store a set of values of any data type.
# The list can contain different types of elements such as int, float, string, Boolean, etc. 

a = [12,2,3,4,5,6,7] 

print(a) #Printing a list
print(a[0]) #Accessing using index
a[0] = 21 #Lists are mutable, therfore there values can be changed
print(a)

# We can create a list with items of different types
b = [23, "str", True, 34.5]

# List Slicing
c = [34,65,23,64,33,"33"]
print(c[0:4])
print(c[-4:])

'''
List Methods
Consider the following list:

L1 = [1, 8, 7, 2, 21, 15]
sort() – updates the list to [1,2,7,8,15,21]
reverse() – updates the list to [15,21,2,7,8,1]
append(8) – adds 8 at the end of the list
insert(3,8) – This will add 8 at 3 index
pop(2) – It will delete the element at index 2 and return its value
remove(21) – It will remove 21 from the last

'''

L1 = [1, 8, 7, 2, 21, 15]
print("List before sorting: ",L1)
L1.sort() #Sorts the list
print("List after sorting: ",L1)

L1.reverse() #Reverses the list
print("List after reversing: ",L1)

L1.append(12) #Adds at the end of the list
L1.append(111)
print("List after appending: ",L1)

L1.insert(0,544) #Inserts 544 at index 2
print("List after inserting: ",L1)

L1.pop(2) #Removes the element at the given index
print("List after popping: ",L1)

L1.remove(21) #Removes the element mentioned
print("List after removing: ",L1)



# L2 = [1, 8, 7, 2, 21, 15]
# print("L2 sorting:",L2.sort())
# print(L2)

# Storing the elements in a tuple

# f1 = input("Enter fruit Number 1: ")
# f2 = input("Enter fruit Number 2: ")
# f3 = input("Enter fruit Number 3: ")
# f4 = input("Enter fruit Number 4: ")
# f5 = input("Enter fruit Number 5: ")
# f6 = input("Enter fruit Number 6: ")
# f7 = input("Enter fruit Number 7: ")

# myFuitList = [f1,f2,f3,f4,f5,f6,f7]
# print(myFuitList)


m1 = int(input("Enter Student's Marks 1: "))
m2 = int(input("Enter Student's Marks 2: "))
m3 = int(input("Enter Student's Marks 3: "))
m4 = int(input("Enter Student's Marks 4: "))
m5 = int(input("Enter Student's Marks 5: "))
m6 = int(input("Enter Student's Marks 6: "))
m7 = int(input("Enter Student's Marks 7: "))

myList = [m1,m2,m3,m4,m5,m6]
print(myList)
print(sum(myList))


