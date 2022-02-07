# Sets in Python -->data types containing unique values.
# Set is a collection of non-repetitive elements.

'''
Properties of Sets-
Sets are unordered # Elements order doesn’t matter
Sets are unindexed # Cannot access elements by index
There is no way to change items in sets
Sets cannot contain duplicate values
'''

a = {1,3,4,5}
print(type(a))
print(a)
a = {1,3,4,5,1}
print(type(a))
print(a)

a1 = {}# This syntax will create an empty dictionary instead of set
print(type(a1))

a2 = set()# This syntax will create an empty set
print(type(a2))
a2.add(4)
a2.add(41)
a2.add(5)
a2.add(6)
a2.add(7)
a2.add(7)
print(a2)

# a2.add([4,5,6]) #unhashable type: 'list'
# List cannot be added inside a set as they are mutable

a2.add((3,4,5))  #hashable type: 'tuple'
# Tuple can be added inside a set as they are immutable

print(a2) 

'''
Operations on Sets
Consider the following set:

S = {1,8,2,3}
len(s) : Returns 4, the length of the set
remove(8) : Updates the set S and removes 8 from S
pop() : Removes an arbitrary element from the set and returns the element removed.
clear() : Empties the set S
union({8, 11}) : Returns a new set with all items from both sets. #{1,8,2,3,11}
intersection({8, 11}) : Returns a set which contains only items in both sets. #{8}
'''
# Length of the set
print(len(a2))

#Removal
a2.remove(41)#Throws an error if the number is not present
print(a2) 

# Popping
print(a2.pop())

# Important
s = {20,20.0,"20"}
print(s)
print(len(s)) #20 and 20.0 are counted same in python. Thus the length is 2 for s
