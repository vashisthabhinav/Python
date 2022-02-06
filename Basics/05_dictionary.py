# Dictionary is a collection of key-value pairs.


from hashlib import md5


myDict = {
    "key": "value",
    "python": "code",
    "marks" : "100",
    "list": [1,2,9],
    "anotherDict": {'Abhinav': 'Vashisth'}
}
print(myDict["list"])

myDict["list"] = [12,21,30]
print(myDict["list"])

print(myDict["anotherDict"]['Abhinav'])


'''
Properties of Python Dictionaries
It is unordered
It is mutable
It is indexed
It cannot contain duplicate keys
'''


# Dictionary Methods
'''
items() : returns a list of (key,value) tuple.
keys() : returns a list containing dictionary’s keys.
update({“friend”: “Sam”}) : updates the dictionary with supplied key-value pairs.
get(“name”) : returns the value of the specified keys (and value is returned here)
'''

myDict = {
    "key": "value",
    "python": "code",
    "marks" : "100",
    "list": [1,2,9],
    "anotherDict": {'Abhinav': 'Vashisth'}
}

# List is just used to type cast the keys and values into a list

print(list(myDict.keys())) #Prints the keys of the dictionary
print(list(myDict.values())) #Prints the values of the dictionary
print(list(myDict.items())) #Prints the (key,values) for all items of the dictionary 

print(myDict)
updateDict = {"friend": "Sam"}
myDict.update(updateDict) #Updates the dictionary by addind key-value pairs
# If any key is already present in the myDict, then the updateDict will update that value. 
print(myDict)

'''
IMPORTANT NOTE:
get() do not returns null if a key pair is not present and it will return null.
'''
print(myDict.get("friend"))
print(myDict["friend"])
# The above two lines of code will give the same result as there is "friend" key present

print(myDict.get("friend1")) #Retuns null as "friend1" is not present
# print(myDict["friend1"]) #Throws an error as "friend1" is not present






