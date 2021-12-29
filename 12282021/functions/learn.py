'''
This is the Syntax for functions:

def functionName(parameters):
    """docstring"""
    statement(s)
    return expression
'''

#1
from typing import Sequence


def fun():
    print("learning is fun :)")
fun()


print(6%2)
#2 
def evenOdd(x):
    if(x % 2 == 0): # print(6%2), if 1, then odd, 0 is even
        print("even")
    else:
        print("odd")
evenOdd(2)
evenOdd(5)

#3
#*kwargs for varriable number of keyword argument
#*args, arbitrary arguments, so if amount of args passed in function not known, add * before parameter name
def tryFunc(*students):
    print("The first student is: " + students[0])

tryFunc("john", "two", "three") # remember, 0 ,, 1 , 2

#*kwargs, arbitrary keyword arguments
def tryFunc(**students):
    print("my student's name is " + students['lname'])

tryFunc(fname = "james", lname= "refefe")
#output
# The first student is: john
# my student's name is refefe

# recursion: meaning defined function can call itself, mainly for math and programming concept

def triRecursion(k):
    if(k>0):
        result = k + triRecursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\n Recursion Example")
triRecursion(6)

# so what is happening from 45 - 53?
# triRecursion is calling itself to "recurse" and the value we have given
# for k is 6.triRecursion which decrements -1 every time we recurse (or loops itself),
# the recurse loop stops when the condition is not greater than 0
# so
# 6 > 0
#     result = 6 + (6-1)
#     prints > 11

#     11 = 5+ ( 5-1) >> 11 = 5 + 4 
#     print > 9

#     9 = 4 + (4-1) >> 9 = 4 + 3
#     print > 7

#     7 = 3 + (3-1) >> 3 + 2 
#     print > 5

#     5 = 2 + (2-1) >> 2+1
#     print >3

#     3 = 1 + (1-1) >> 1
#     print 1 

#     this is when is 0
#     so it just returns result


#     ooooh i think i had it backwards, it starts from 0
#     result = 0 + (0-1)
#     print = doesn't print anything, i think

#     result = 1 + (1-1)
#     print = 1

#     result 2 + 2-1 
#     print 3

#     result 3 + 3-1
#     print 5
#     yeah, this is iter
    
#     result 4 + 4-1
#     7

#     result 5 + 5-1
#      hmmm i guess i didn't understand it 

# try again
#     so value is 6

#     6 > 0 = True
#         result = 0 + fn(0-1)
#         print= nothing, because there isn't in -1

#     6 > 1 = True
#         result 1 + fn(1-1)
#         print = 1
#     6 > 2 = True
#         result 2 + fn(2-1) > 1+ 3
#         print = 3
#     yeah i think this is the Sequence
#     6 > 3 = True
#         result 3 + fun(3-1) >> 3 + 3  
#         print = 6
#     6 > 4 = True
#         result 4 + fun(4-1) >> 4 + 6
#         print = 10

#     6 > 5 = True
#         result 5 + 10 
#         print 15
#     6 > 6 = true / i guess??
#         result 6 + 15
#         print 21
#     6 > 7 = false / meaning 0
#         retrun results