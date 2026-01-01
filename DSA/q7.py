class Solution:
    def solve(self, A):
        k = "AEIOU"
        m = "aeiou"
        l = []
        for j in A:
            if j in k or j in m:
                l.append(j)
        sorted_data = sorted(l, key=lambda x: (x.upper(), x.islower()))
        A = list(A)
        index = 0
        for char in A[:]:
            if char in k or char in m:
                A[index] = sorted_data.pop(0)
            index += 1
        return ''.join(A)

A = "leetcode"
result = Solution().solve(A)
print(result)
