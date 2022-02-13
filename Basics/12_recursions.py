# Recursive approach for factorial
'''
Recursion is a function which calls itself.
    It is used to directly use a mathematical formula as a function.

'''
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)
print(factorial(7))

def removeAndStrip(string, word):
    newStr = string.replace(word,"")
    return newStr.strip()

a = "           My Name is Abhinav Vashisth         "
n = removeAndStrip(a,"My")
print(n)
print(a)
print(a.strip())