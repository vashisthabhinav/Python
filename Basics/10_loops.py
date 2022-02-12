'''
Types of loops in Python
Primarily there are two types of loops in Python

While loop
For loop
'''

# While
i = 0
while i<=50:
    print(str(i))
    i = i+1

print("Done")

'''
In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed, otherwise not!

If the loop is entered, the process of condition check and execution is continued until the condition becomes false.
'''

list1 = ['1','2','3','4','5','6','7','8','9','10']
i1 = 0
while i1 <len(list1):
    print(list1[i1])
    i1 = i1+1
fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i+1
# For
'''
A for loop is used to iterate through a sequence like a list, tuple, or string (iterables)
'''
print("\nFor Loop")
l = [1, 7, 8]
for item in l:
	print(item)

# Range Function in Python
print('Range Function in Python')
'''
The range function in python is used to generate a sequence of numbers.

We can also specify the start, stop, and step-size as follows:

            range(start, stop, step_size)

step size is usually not used with range()
'''

for j in range(-2,8):
    print(j)


for j in range(-2,8,2):
    print(j)

# For loop with else
print('For loop with else')
'''
An optional else can be used with a for loop if the code is to be executed when the loop exhausts.
'''
l = [1,2,3,4,5,6,7,8,9,10]
for item in l:
	print(item)
else:
	print("Done")	#This is printed when the loop exhausts!

# Break
'''
‘break’ is used to come out of the loop when encountered. It instructs the program to – Exit the loop now.
'''

print('Break')
for i in range(0, 80):
	print(i)	#This will print 0, 1, 2 and 3
	if i == 30:
		break
else:
	print("This is inside else of 'for' loop")	#This is not printed due to break 

# The continue statement
print('The continue statement')
'''
‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the program to “skip this iteration.”
'''


for i in range(4):
	print('printing')
	if i == 2:	#if i is 2, the iteration is skipped
		continue
	print(i)

# pass statement
print('pass statement')
# pass is a null statement in python. It instructs to “Do nothing.”

l = [1, 7, 8]
for item in l:
	pass		
#without pass, the program will throw an error

i = 4
if i>0:
    pass
    print('Pass Statement')

# Practice

# For loop
num = int(input('Enter a number: '))
for i in range(1,11):
    # print(str(num)+' X '+str(i)+' = '+str(i*num) )
    print(f"{num} X {i} = {num*i}") # F-string

# While loop
num = int(input('Enter a number: '))
j = 1
while j<=10:
    print(f"{num} X {j} = {num*j}") # F-string
    j = j+1

l1 = ["Nikhil", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)


num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is composite")



num = int(input("Enter the number: "))
i = 0
sum = 0
while i<=num:
    sum = sum+i
    i = i+1

print(sum)

#n! = 1 X 2 X 3 X ..... X n
#5! = 1 X 2 X 3 X 4 X 5



num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")

num = int(input("Enter the number: "))
for  i in range(num):
    print('*'*(i+1))


n = 3
for i in range(3): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))

num = int(input('Enter a number: '))
j = 10
while j>=1:
    print(f"{num} X {j} = {num*j}") # F-string
    j = j-1