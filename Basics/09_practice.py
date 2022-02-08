# Pass
'''
In Python, pass is a null statement. 
The interpreter does not ignore a pass statement, but nothing happens and the statement results into no operation.
The pass statement is useful when you don’t write the implementation of a function but you want to implement it in the future.
'''

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else: 
    f1 = num4
if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f2)+" is the winner ")
else:
    print(str(f1)+" is the winner ")

sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))
total = int(input("Enter maximum subject marks\n"))
if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif((sub1+sub2+sub3)*100)/(3*total) < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations! You passed the exam")


    