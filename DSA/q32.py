class Solution:
    def singleNumber(self, nums):
        nums.sort()
        for i in range(1,len(nums)) :
            if nums[i] == nums[i-1] :
                return True
        return False

nums = [3,3]        
Solution = Solution()
result = Solution.singleNumber(nums)
print(result)