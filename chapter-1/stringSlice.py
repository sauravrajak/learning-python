"""
Slicing
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.

indexing[] slicing[]
[start:stop:step]

"""

name = "Saurav Kumar"

myFirstName = name[0:6]
myLastName = name[7:13]
print(myFirstName)
print(myLastName)

print(name[:7])