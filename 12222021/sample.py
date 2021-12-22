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

# combine both text and variable using the '+' character
# this can also can be added variable to variable, 

x = "hello"
print(x + " john") # prints hello john

x = 5
y = 10
print(x+y) # prints 15 

# BUTTTTT you cannot combine string and a number, otherwise it will give you error!!!

#global variables, created outside of a function where everyone both inside and outside 
# a function can access


# begin example
x = "johnny"
def myfunc():
    print(" hello" + x)
myfunc()

print("python is " + x)

# end example

# you can also use 'global' keyword
def myfunc():
    global y
    y = "globall Y" # haha i so funny
myfunc()

print("hello " + y)

# by doing global, you can also change a global variable inside a function

a = "ABC"
print(a) # so this hasn't been changed yet
def myfunc():
    global a
    a = "xyz" # variable a changes here
myfunc()
print("learning my " + a) # this prints out learning my xyz