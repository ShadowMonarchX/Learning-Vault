class Solution:
    # @param A : integer
    # @return a integer
    def solve(self, A):
        if A == 0:
            return 1  # Factorial of 0 is 1
        r1 = 1
        for i in range(1, A + 1):
            r1 *= i  # Multiply r1 by i in each iteration
        return r1  # Return the factorial

Solution = Solution()
A = 10
result = Solution.solve(A)
print(result)
