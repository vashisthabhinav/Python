# File I/O

'''
The random access memory is volatile, and all its contents are lost once a program terminates.
In order to persist the data forever, we use files.
A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.
Types of Files-
    There are 2 types of files:
        Text files (.txt, .c, etc)
        Binary files (.jpg, .dat, etc)
'''

f = open('sample.txt','r') #Opens the file in r mode
data = f.read() #Read its content
print(data) #Print its contents
f.close()#Close the file

# We can also use f.readline() function to read one full line at a time.

# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)

'''
Modes of opening a file
    r – open for reading
    w – open for writing
    a – open for appending
    + -> open for updating

‘rb’ will open for read in binary mode

‘rt’ will open for read in text mode
'''

'''
Writing Files in Python
    In order to write to a file, we first open it in write or append mode, after which, we use the python’s f.write() method to write to the file!
'''

f1 = open('Another.txt','w')
f1.write("Please write this to the file\n")
f1.close()
f1 = open('Another.txt','a')
f1.write("Please write this to the file\n")
f1.close()
f1 = open('Another.txt','a')
f1.write("Please write this to the file\n")
f1.close()
f1 = open('Another.txt','a')
f1.write("Please write this to the file\n")
f1.close()
f1 = open('Another.txt','a')
f1.write("Please write this to the file\n")
f1.close()
f1 = open('Another.txt','a')
f1.write("Please write this to the file\n")
f1.close()
f1 = open('Another.txt','a')
f1.write("Please write this to the file\n")
f1.close()
f1 = open('Another.txt','a')
f1.write("Please write this to the file\n")
f1.close()
f1 = open('Another.txt','a')
f1.write("Please write this to the file\n")
f1.close()

# With Statement
# The best way to open and close the file automatically is the “with” statement.
with open('With.txt','a') as f2:
    f2.write("Please write this to the file\n")