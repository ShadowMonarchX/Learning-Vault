
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) ->float:
        add = nums1 + nums2
        add.sort()
        x = len(add)
        if x%2 == 0 :
            z = int(x/2)
            y = add[z] + add[z-1]
            return y/2
        else :
            return float(add[int(len(add)/2)])

Solution = Solution()
nums1 = [1,3]
nums2 = [2]
result = Solution.findMedianSortedArrays(nums1,nums2)
print(result)