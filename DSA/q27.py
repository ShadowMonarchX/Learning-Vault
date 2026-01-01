from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        new_index = 0
        ans = 0
        n = len(nums)
        for i in range(0,n) :
            if nums[i] == 0 :
                count += 1
            while count > 1 :
                if nums[new_index] == 0 :
                    count -= 1
                new_index += 1
            out = i - new_index + 1 - count
            ans = max(ans , out )

        if ans == n :
            return ans - 1
        else :
            return ans

nums = [0,1,1,1,0,1,1,0,1]    
Solution = Solution()
result = Solution.longestSubarray(nums)
print(result)