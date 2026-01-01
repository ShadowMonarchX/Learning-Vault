from typing import List
from itertools import combinations

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        list_new = set()
        for i in range(0,len(nums)-3):
            for j in range(i+1,len(nums)-2) :
                for k in range(i+2,len(nums)-1):
                    for m in range(i+3,len(nums)) :
                        if nums[i]+ nums[j] + nums[k] + nums[m] == target :
                            list_new.add(tuple(sorted((nums[i],nums[j],nums[k],nums[m]))))
                            new_l = list(list_new)
        ans = []
        for i in range(0,len(new_l)):
            k = list(new_l[i])
            ans.append(k)
        return ans
        
#this answer is not valid beause time complecty error and O(n**3) requer this time complexty 
nums = [1,0,-1,0,-2,2]
target = 0
Solution = Solution()
result = Solution.fourSum(nums,target)
print(result)