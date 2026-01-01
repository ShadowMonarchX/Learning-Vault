
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        nums1 = []
        
        for i in range(0,n):
            sum = 0
            if len(nums) > 2 :
                for j in range(0,2) :
                   sum += nums[j]
            nums.remove(nums[i])
            nums1.append(sum)
             

        return nums1
        for i in range(0,n):
            count = False
            for j in range(0,n-i) :
                if nums[j] > nums[j+1] :
                    nums[j] , nums[j+1] = nums[j+1] , nums[j] 
                    count = True
            if not count :
                break
        if len(nums) >= 3 :
            out = nums[0] + nums[1] + nums[2]
        else :
            out = 0
        
        return out
        

nums = [-1,2,1,-4,2,3,4]
target = 1
Solution = Solution()
result = Solution.threeSumClosest(nums,target)
print(result)