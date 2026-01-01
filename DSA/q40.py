class Solution:
    def rotate(self, nums, k):
        k = k % len(nums) 
        r = len(nums) - k
        new1 = nums[0:r]
        nums[0:r] = []
        new2 = []
        for i in range(-1,-(1+len(nums)),-1) :
            new2.append(nums[i])
        nums.extend(new1)
        return new2 + new1
nums = [1,2,3,4,5,6,7,8,9]



k = 7
s1 = Solution()
result = s1.rotate(nums,k)
print(result)