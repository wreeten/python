class Solution(object):
    def twoSumLTk(self, A, k):
        ans = -1
        if len(A)==1:
            return -1
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                temp=A[i]+A[j]
                if temp<k:
                    ans=max(ans,temp)
            return ans
ob1 = Solution()
print(ob1.twoSumLTk([34,23,1,24,75,33,54],60))
