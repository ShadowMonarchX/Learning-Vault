class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while len(s) > i and len(t) > j :
            if s[i] == t[j] :
                i += 1
            j += 1
        
        return len(s) == i
Solution = Solution()
s = "abc"
t = "ahbgdc"
result = Solution.isSubsequence(s,t)
print(result)