from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for the position to place non-val elements
        k = 0
        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != val:
                # Place the current element at the position k
                nums[k] = nums[i]
                k += 1
        return k


nums = [3, 2, 2, 3]
val = 3
solution = Solution()
k = solution.removeElement(nums, val)
print("Output k:", k)         # Output k: 2
print("Modified nums:", nums) # Modified nums: [2, 2, _, _]


