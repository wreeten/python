# This is an example of two sum array data structure to better understand it.
#A = [-2, 1, 2, 4, 7, 11] # so we need to get numbers from this array to get to target value, 13
#target = 13

#Time complexity is 0(n^2)
#space complexity is 0(1)
def two_sum_brute_force(A,target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i],A[j]) # this prints out the values added 
                return True
    return False
#print(two_sum_brute_force(A,target))

#example two

#A = [2, 4, 6]
#target = 10

#i = 0 # first index of our loop
#ht = dict()
#ht[8] = 2

#i = 1
#ht[6] = 4


b = [2, 4, 6]
target = 10
def two_sum_hash_table(b, target):
    ht = dict()
    for i in range(len(b)):
        if b[i] in ht:
            print(ht[b[i]], b[i])
            return True
        else:
            ht[target - b[i]] = b[i]
    return False
print(two_sum_hash_table(b,target))

A = [-2, 1, 2, 4, 7, 11]
target = 13
#TC = O(n)
#SC = 0(1)
def two_Sum(A,target):
    i = 0
    j = len(A) -1

    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:# A[i] + A[j] < target
            j -= 1
    return False

print(two_Sum(A,target))
