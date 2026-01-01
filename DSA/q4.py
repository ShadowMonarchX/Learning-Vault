class Solution:
    def solve(self, A, B):
        a = min(len(A),len(B))
        b = max(len(A),len(B))
        k = ""
        for i in range(0,a) :
            for j in range(0,b) :
                if A[j] == B[i] and j == i:
                    k = k + A[j]
        if k == None :
            return ""
        else :
            return k

A = "ABABAB"
B = "ABAB"
result = Solution().solve(A, B)
print(result)
