# def digitSum(n):
#     dsum = 0 
#     for ele in str(n): # elements in "n" are converted to string
#         dsum += int(ele) # dsum increments for each element
#     return dsum

# List = [ 333, 111, 562, 945, 6343,834]

# newList = [digitSum(i) for i in List if i & 1] # the values in i in digit sum for that are in LIST 

# print(newList)

#nested if
i = 10
if (i == 10):
        if (i < 15):
            print("i is smaller than 15")

        if(i < 12):
            print("i is also smaller than 12")
        else:
            print("greater than 15")