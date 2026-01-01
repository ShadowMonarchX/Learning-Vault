from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 += nums2
        element = 0
        for i in nums1 :
            print(i)
            if element in nums1 :
                nums1.remove(element)
        nums1.sort()
        print(nums1)

Solution = Solution()
nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,3,4,5]
n = 5
m = 0
result = Solution.merge(nums1,m,nums2,n)