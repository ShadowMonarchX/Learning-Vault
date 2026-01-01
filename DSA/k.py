from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_count = max(counts.values())
        for num, count in counts.items():
            if count == max_count and count > len(nums)/2:
                return num
        
Solution = Solution()
nums = [3,3,4]
result = Solution.majorityElement(nums)
print(result)
            