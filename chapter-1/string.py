"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.
"""
name = "Saurav Kumar"

print(name.count('a'))
print(name.replace("S","G"))
print(name.capitalize())
print(name.upper())
print(name.casefold())
print(name.__contains__("Sa"))


"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.

"""

a = "Hello World"
print(a[0])  # --> It will print H

