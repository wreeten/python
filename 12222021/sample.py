#started 1222021 1:00pm
print("Hello World")
if 5>2:   # python syntax, you have to use : at the ned
    print("5 is greater than 2") # also the amount of spaces/tabs matter or else it will give you error
x = 5; # this is assigning a value to a variable
y = "hello world" # assigning value to variable y, in this case this is a string

# multi line code is " " "    { }  " " "  where {  } is stuff inside the multi line code

print(x) # will output 5
print(y) # will output hello world
""" 
x = str(3) this is '3'
y = int(3) this is 3
z = float(3) this is 3.0
"""
# what this does is that it gets the data type variable with this type() function
print(type(x)) # <class 'int' >
print(type(y))  # <class 'str' >

#in python, variables can be declared as single or double quotes
# variables are case sensitiveS

"""
variables start with a later or underscore, cannot start w/ number, CASE SENSITIVE! 
these are ILLEGAL:
2myvar=1
my-var = 1
my var = 1

camel case: each first letter of word except first is capital
myVariableName = "1"

pascal case : each word starts with capital case
MyVariableName = "1"

snake case, each word separated by underscore
my_variable_name = "1"
"""

# many values to multiple variuables
x, y, z = "orange", "ap", "three"
print(x,y,z) # prints, orange ap three

# one value to multiple variables
x = y = z = "orange"
print(x, y ,z) # prints orange orange orange

#unpacking the collection
fruits = ["ap", "ban", "che"]
x,y,z = fruits
print(x)
print(y)
print(z)

