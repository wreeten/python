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

"""
DATA TYPES 1:43

text : str >> "hello world"

numeric: int, float, complex >> 20 >> 20.5 >> 1j

sequence types: list, tuple, range >> x = ["ap", "ban", "cher"] >> ("ap", "ban", "cher") >> range(6)

mapping type: dict >> x = {"name" : "john", "age" : 01}

set types: set, frozenset >> {"ap", "ban", "cher"} >> x = frozenset({"ap", "ban", "cher"})

boolean type: bool >> x = True

binary : bytes, bytearray,memoryview >> x = b"hello" >> bytearray(5) >> memoryview(bytes(5))

type() function to get the type of any object
you can use print(type(x))

"""

"""
NUMBERS 

integers: whole numbers, pos, or neg, without decimals

float: number, pos or neg, containing one or more decimals
can also be scientific numbers with "e"
example:
x = 35e3
or
z = 86.2e100

complex. written with j as the imaginary part
x = 3 + 5j


TYPE CONVERSION

x = 1 # int
y = 2.8 # float
z = 1j # complex


a = float(x) # this converts from int to float in variable a >> 1.0
b = int(y) # convert float to int >> 2
c = complex(x) >> (1 + 0j)

x = int(#)
x = float(1)
x = str(2) # will be '2'
"""

# multiline string is similar to the multi line comments
a = """ blah
blah
blah this 
is multiline """
print(a)

#strings are arrays representing unicode character, and single char is a string with lenght of 1

a = "hello world"
print(a[1]) # this prints out 'e' because h is position 0

#loop through a string, 
for x in "banana":
    print(x) # this prints out a concatanation of banana(1 x 6)
a = "hello world"
print(len(a)) # this prints out 11, becauus "a = "hello world"" has value of 11 lol

#check string,
print( "hello" in a) # this comes out as a boolean to test if "hello" is a string, outputs True

# this checks if 'hello' is present
if "hello" in a:
    print("yes, 'hello' is here")

#if NOT, this checks if string is not present
if "cute" in a:
    print("cute" not in a) # if cute is not in 'a' then it doesn't do anyhting, if it is OP is false

if "cute" not in a:
    print("no cute is NOT prsent")


#sliiiicinggggg , returns a range of characters 

b = "hello, mother"
print(b[2:5]) #gets position 2-5, so llo is printer ONLY CCHARACTERS not the comma

print(b[:5]) # position beginning to posiion 5, OP hello

print(b[2:]) # prints from 2 to the end

print(b[-5:-2]) # prints out 'oth'

#uppercasing things

a = "hello, mother"
print(a.upper()) # creams above
print(a.lower()) # whispers

print(a.replace("h","j")) # replaces H with J, so this prints jello motjer

print(a.split(",")) # returns ['hello, mother']

#concatenate, u use +


# remember before we cannot combine strings and numbers, so the best way to combine this is with format

age = 999
txt = "my name is john and {}" # the {} is the placeholder
print(txt.format(age))

qt=  3
item =555
price = 39.99
myorder="I want {} pieces of item {} for {} dollars"
print(myorder.format(qt, item, price)) # oooohhh this i scooooool


# you can use index numbers {0} for places in right placeholders
myorder="I want {2} pieces of item {0} for {1} dollars"
print(myorder.format(qt,item,price)) #ooooh, so it does price first, then qt, then item

# if you want to use illegal characters like "vikings", then you need to do the \ thing 
# txt = "we are so called "engineers" "  this wont print because of the double quotes inside
#txt = "we are so called \"engineers\" " // to make this possible you need to add

# /*
# this \' > single quotes
# this \\ backslash
# this \n new line
# this\r carroage retirn
# this\t tab
# \b backspace
# \f form feed
# \ooo octal value
# \xhh hex value
# */


#ctrl + / does this comment, so you highlight then press that command then it does multi line!!
# BOOOOOLEANNNNSSSS

print (10 > 9)