"""
User Input
Python allows for user input.
That means we are able to ask the user for input.
The method is a bit different in Python 3.6 than Python 2.7.
Python 3.6 uses the input() method.
Python 2.7 uses the raw_input() method.

"""
# it always takes string value as user input 
name = input("What is your name ? ")
print(f"Hello {name}")


# we canot perform math on a string 
# so we have to typecast into integer

x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))

print(x+y)


