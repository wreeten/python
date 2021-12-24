# # this is an example of when it's best to buy and sell stock 

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# so profit is 6-1 = 5
# time moves in one direction, so we cannot sell at 7 -1.

#this is an example of POINTERS
#LEFT and RIGHT
#left is day we buy, right is day we sell
# memory 0(1) time : 0(n)


# class Solution:
def maxProfit(self, prices: list[int]) -> int:
    l, r = 0, 1 # left = buy, right = sell
    maxPrice = 0

    while r <len(prices):
        #profitable?
        if prices[l] <prices[r]:
            profit=prices[r] -prices[l]
            maxPrice = max(maxPrice,profit)
        else:
            # 1 += 1 you dont want to shift it only by one, but all the way to the right, so
            l = r
        r += 1
    return maxPrice
    
    