# Strings In Python
'''The string is a data type in Python.

A string is a sequence of characters enclosed in quotes.

We can primarily write a string in three ways:

Single quoted strings : a = 'Abhinav'
Double quoted strings : b = "Abhinav"
Triple quoted strings : c = ‘’’ Abhinav ‘’’
'''
from operator import le


a1 = "India's" #--> Used when single quotes are to be used in the string
a2 = 'He quoted-"Hello"' #--> Used when double quotes are to be used inside the string
a3 = ''' He quoted-
"India's" ''' # Used when both single and double quotes are to be used in a string and when we have to use a mutliline string


'''String Slicing:
A string in Python can be sliced for getting a part of the string.'''


# Concatenating two strings
b1 = "Good"
b2 = " morning!!"
b3 = b1 + b2
print(b3)

# String Slicing
# The index in a string starts from 0 to (length-1) in Python. 
print(b3[10]) #--> Accessing an index of a string
'''
NOTE:
We can only access the strings and its indices
We cannot change it
Strings are immutable just like Java
'''
print(b3[1:11]) #Means it will print the string from [0,10) -->10th index not counted
print(b3[:11]) #Starts from 0 by default
print(b3[4:]) #Ends at the last index by default

'''
Negative Indices: Negative indices can also be used as shown in the figure above. -1 corresponds to the (length-1) index, -2 to (length-2).
'''
b4 = "Abhinav"
b5 = b4[-5:-1]
print(b5)

'''licing with skip value

We can provide a skip value as a part of our slice. '''

c1 = "Abhinav Vashisth"
c2 = c1[1:5:1] #-->Skips one character
print(c2)
c3 = c1[1::2] #-->Skips two characters
print(c3)

# String Function
'''String Functions
Some of the most used functions to perform operations on or manipulate strings are:

len() function : It returns the length of the string.
len(‘harry’)               #Returns 5
endswith(“rry”) : This function tells whether the variable string ends with the string “rry” or not. If string is “harry”, it returns for “rry” since harry ends with rry.
count(“c”) : It counts the total number of occurrences of any character.
capitalize() : This function capitalizes the first character of a given string.
find(word) : This function finds a word and returns the index of first occurrence of that word in the string.
replace(oldword, newword) : This function replaces the old word with the new word in the entire string.'''

movie = "once upon a Time in Mumbai"

print(len(movie))
print(movie.endswith("bai"))
print(movie.count("a"))
print(movie.capitalize())
print(movie.find("in"))
print(movie.find(" ")) #First Occurance
print(movie.replace("once","Twice")) 
print(movie.replace(" ","&nbsp;")) #All the occurances

# Escape Sequence Characters
'''Escape Sequence Characters:
Sequence of characters after backslash ‘\’ [Escape Sequence Characters]

Escape Sequence Characters comprises of more than one character but represents one character when used within the string.

Examples: \n (new line), \t (tab), \’ (single quote), \\ (backslash), etc.
'''
print("My\tname is \n Abhinav \\Vash\'isth")


# Important

letter = '''
        Dear <|NAME|>,
        You are selected.
        
        Date : <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)
