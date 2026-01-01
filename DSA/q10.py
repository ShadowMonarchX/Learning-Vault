from typing import List
from itertools import combinations

class Solution:
    def productExceptSelf(self, nums: List[int]):
        n = len(nums1) - 2
        result = []
        k = []
        for i in range(0,n) :
            result = nums[i:i+3]
            if result[2] > result[1] and result[1] > result[0] :
                k.append(True)
            else :
                k.append(False)
        m = []
        count = 0
        print(k)
        for i in range(0,n) :
            if k[i] == True :
                return True
            else :
                count += 1
            if count == n :
                return True
        return False

Solution = Solution()
nums2 = [5,4,3,2,1]
nums1 = [20,100,10,12,5,13]
result = Solution.productExceptSelf(nums1)
print(result)