class Solution:
    def solve(self, A, B):
        r1 = list(A)
        r2 = list(B)
        r3 = [r1, r2]
        r4 = []
        sum = ""

        max_len = 0
        for sublist in r3:
            print(len(sublist))
            if len(sublist) > max_len:
                max_len = len(sublist)
        print(max_len)
        for i in range(max_len):
            for sublist in r3:
                if i < len(sublist):
                    r4.append(sublist[i])
        a = min(len(r1),len(r2))
        for i in range(0,a):
            if r[i] == r[i+1]:
                pass
        return sum

A = "abcd"
B = "ef"
result = Solution().solve(A, B)
print(result)
