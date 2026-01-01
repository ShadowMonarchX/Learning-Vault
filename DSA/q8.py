class Solution:
    def solve(self, A):
        words = s.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string
        
A = "leetcode a very   beutiful"
result = Solution().solve(A)
print(result)
