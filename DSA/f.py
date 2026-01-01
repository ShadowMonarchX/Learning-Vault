class Solution :
    def optimazialDivision(self,nums) :
        nums1 = str(nums[0])
        nums2 = nums[1:]
    

        for num in nums2:
            num = str(num)
            num += num
        print(num)


S1 = Solution()
nums = [1000,100,10,2]
result = S1.optimazialDivision(nums)
print(result)


