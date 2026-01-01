from typing import List
from itertools import combinations

class Solution:
    def findMedianSortedArrays(self, nums1,a) ->float:
        c = max(nums1)
        x = []
        for i in nums1 :
            if i + a >= c :
                x.append(True)
            else :
                x.append(False)
        return x
Solution = Solution()
nums1 = [2,3,5,1,3]
a = 3
result = Solution.findMedianSortedArrays(nums1,a)
print(result)