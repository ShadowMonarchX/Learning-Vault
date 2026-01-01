class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(nums[i-1]))
                start = nums[i]

        # Handle the last range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(nums[-1]))

        return ranges

S1 = Solution()
nums = [1,2,5,6,7

,9]
r = S1.summaryRanges(nums)
print(r)