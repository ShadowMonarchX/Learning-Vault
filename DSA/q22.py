from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left,right=0,len(nums)-1
        count = 0
        while left < right:
            temp = 0
            temp = nums[left] + nums[right]
            if temp == k :
                count += 1
            left += 1
            right -= 1

        return count

nums =[4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2
Solution = Solution()
result = Solution.maxOperations(nums,k)
print(result)