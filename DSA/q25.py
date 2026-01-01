class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return 0

        max_count = 0
        current_count = 0

        for i in range(k):
            if s[i] in "aeiou":
                current_count += 1

        max_count = current_count

        for i in range(k, n):
            if s[i - k] in "aeiou":
                current_count -= 1
            if s[i] in "aeiou":
                current_count += 1
            max_count = max(max_count, current_count)

        return max_count
s = "abciiidef"
k =  3
Solution = Solution()
result = Solution.maxVowels(s,k)
print(result)