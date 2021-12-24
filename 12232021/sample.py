#15:32 , okay i forgot. so if I want to comment multiple blocks, I can highlight then ctrl + /
# cards= [13, 11, 10, 7, 4, 3, 1, 0]
# query = 7
# output = 3

#since we'll have multiple test samples we can create a dictionary to make it easier to test them once we write our function




#this is the same as lines 2 - 4
# test = {
#     'input':{
#         'cards':[13,11,19,7,4,3,1,0],
#          'query':7
#     },
#     'output':3
# }


# result = locate_cards(cards, query)
# print(result)
# locate_cards(**test['input']['cards']) == test ['output']


# tests = [] # creating an array called tests
# tests.append(test)

# tests.append({
#     'input': {
#         'cards':[13,11,10,7,4,3,1,0],
#         'query':1
#     },
#     'output': 6
# 
# slice - slice out substrings, sublits,subtples using indexes
#slicing: [start: end+1: step]


#started watching this video for this part: https://youtu.be/kQDxmjfkIKY | 15:50
x = 'computer'
print(x[1:4]) # output omp , the reason why is that start is inclusive and end is NON INCLUSIVE
print(x[1:6:2] ) # output > opt, reason, starts with first char inclusive, to 6 last char non inclusive, step 2
print(x[3:]) #puter3rd item to the end
print(x[:5]) #compu , start string to the last char non inclusive
print(x[-1]) # r,last item of the string
print(x[-3:]) # ter, last 3 elements
print(x[:-2]) # comput, beginning until the last 2 items

#VT = video time
#adding /concatinating - which is combination of 2 sequences  : 7:16 VT

#string
x = 'horse' +'shoe'

#list
y = ['pig','cow'] + ['horse']
print(y)

z=('Jay', 'Kay', 'Ell') + ('Em',) # you have to include ',' after em because it differentiates list and tuple
print(z)

#what is the difference between tuple and list?
# list is mutable, tuple is not. meaning lists can change wheras tuple cannot.


#multiplying 7:30 VT
x = 'bug' * 3
print(x) # bugbugbug

#list
y=[8,5] * 3
print(y)  #[8,5,8,5,8,5]

#tuple
z=(2,4) *3
print(z) #(2,4,2,4,2,4)

#checking membership -tests whether an item is or not in sequence

x = 'bug'
print('u' in x) #true , because U is in X

#list
y=['a','b','c']
print('b' not in y) # false, because B is IN  y

z = ('1','2','3')
print('3' in z) #true, because 3 is in z

#iteration - through items in a sequence 9:12 VT
#item
x= [7,8,3]
for item in x:
    print(item)
# 7
# 8
# 3
#index and item
y = [7,8,3]
for index, item in enumerate(y):
    print(index,item)
# 0 7
# 1 8
# 2 3

# to count number of items in seuqnce, you use len() function

print(len(y)) # result is 3

#find the minimum / lexicographically, alpha or numeric, cannot be mix types 10:18VT
x = 'bug'
print(min(x)) #b
#list
y = ['pig','cow'] + ['horse'] #cow , c comes first alphabet
print(min(y))

z=('Jayeee', 'Kaye', 'Ellssssss') # you have to include ',' after em because it differentiates list and tuple
print(min(z))

# same as max print(max(x))