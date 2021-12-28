# to delete all lines in vim, the command is ':1,$d'
#this is to replace elements with greatest elements on the right
class Solution(object):
    def replaceLMNT(self, arr):
        size = len(arr)
        currMax = -1
        for i in reversed(xrange(len(arr))):
            arr[i],currMax = currMax,max(currMax,arr[i])
        return arr
obj1 = Solution()

def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i])

arr = [ 16,23,4,6,2]
replaceLMNT(arr)
printArray(arr)
