from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        ans = 0
        while left < right:

            if height[left] < height[right]:

                temp = height[left] + (right - left)
                left += 1

            else: 
                temp = height[right]*(right - left)
                right -= 1

            if temp > ans:
                ans = temp
        return ans

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Solution = Solution()
result = Solution.maxArea(height)
print(result)
