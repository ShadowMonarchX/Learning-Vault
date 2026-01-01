
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_value = float("-inf")
        for i in range(n-1,-1,-1):
            m = []
            for j in range(0,i) :
                k = prices[i] - prices[j]
                if k > max_value :
                    max_value = k
        if max_value > 0:
            return max_value
        else :
            return 0

Solution = Solution()
prices = [7,1,5,3,6,4]
result = Solution.maxProfit(prices)     
print(result) 