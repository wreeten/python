# print("\nList Iteration")
# l = ["john", "kay","lol"] # similar to tuple, excpet this would be in parenthesis
# for i in l:
#     print(i)

# print("\n string iteration")
# l= "johnny"
# for i in l:
#     print(i)

# #for dictionary
# print("\nfor dictionary")
# d = dict()
# d['abc'] = 123
# d['def'] = 456
# for i in d:
#     print("% s % d" % (i, d[i])) # %s is string %d is integers #f floating points %x integers in hex rep

# #dictionary part two
# a = dict()
# a["john"] = 111
# a["senior"] = 222
# for i in a:
#     print("%s %d" % (i, a[i]) )

# # # the letters will print except for these values
# # for letter in 'john johssn 1dvcs9': # oh nice so this takes account the spaces

# #     if letter == 'j' or letter == 's':
# #         continue # remember, continues  until there is nothing left in the string
# #     print('current letter :', letter)

# # the letters will stop one it gets to this value
# # for letter in 'john johssn 1dvcs9': # oh nice so this takes account the spaces

# #     if letter == 'h' or letter == 's':
# #         break
# #     print('current letter :', letter) 
# #     # so it will print j then o, but stops at h, Output = j o 

# # this will output thje last letter in the string
# for letter in 'john johssn 1dvcs9': 
#        pass
# print('current letter :', letter) # so the output is 9


# for i in range(10):
#     print(i, end=" ")

l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end =" ")
print()

sum = 0
for i in range(1,10):
    sum += i
print("sum first 10 # : ", sum) # this add's 0 - 9, 0 + 1 +2 +3+4+5+6+7+8+9