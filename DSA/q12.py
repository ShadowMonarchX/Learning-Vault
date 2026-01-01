class Solution :
    def binaryNumber(self,num) :
        power = 1
        ans = 0
        while num > 0:
            rem = num % 2
            num = num // 2
            ans +=(rem * power)
            power *= 10
        return ans

num = 10
Solution = Solution().binaryNumber(num)
print(Solution)