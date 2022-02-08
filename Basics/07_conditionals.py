'''
In python programming too, we must be able to execute instructions on a condition(s) being met. This is what conditions are for!

If else and elif in Python
If else and elif statements are a multiway decision taken by our program due to certain conditions in our code.
'''

a = int(input("Enter your age: \n"))
# If-elif-else ladder
if(a<18):
    print("You cannot vote\n")
elif(a>=18):
    print("You can vote\n")


# Relational Operators
'''
Relational operators are used to evaluate conditions inside if statements. Some examples of relational operators are:

= = -> equals

>=  -> greater than/equal to

<=, etc.
'''

# Logical Operators

'''
Logical Operators
In python, logical operators operate on conditional statements. Example:

and -> true if both operands are true else false

or -> true if at least one operand is true else false

not -> inverts true to false and false to true
'''
# elif clause
'''
elif in python means [else if]. 
If statement can be chained together with a lot of these elif statements followed by an else statement.

'''

# NOTE:
# There can be any number of elif statements.
# Last else is executed only if all the conditions inside elifs fail.