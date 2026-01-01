class Solution :
    def serchInesrt(self,nums,target):
        n = len(nums) - 1
        index = 0
        for i in range(0,len(nums)):
            if target == nums[i]:
                index = i
            else :
                index = index
        if index > 0 :
            return index
        else :
            nums.append(target)
            nums.sort()
        for i in range(0,len(nums)):
            if target == nums[i] :
                return i

Solution = Solution()
nums = [1,3,5,6]
target = 2
result = Solution.serchInesrt(nums,target)
print(result)