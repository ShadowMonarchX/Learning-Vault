from typing import List

def maxset(A: List[int]) -> List[int]:
    ans = []
    cur_ans = []
    max_sum = float('-inf')
    cur_sum = 0
    n = len(A)

    for i in range(n):
        if A[i] >= 0:
            cur_sum += A[i]
            cur_ans.append(A[i])
        else:
            if cur_sum > max_sum or (cur_sum == max_sum and len(cur_ans) > len(ans)):
                max_sum = cur_sum
                ans = cur_ans[:]
            cur_sum = 0
            cur_ans = []

    if cur_sum > max_sum or (cur_sum == max_sum and len(cur_ans) > len(ans)):
        ans = cur_ans

    return ans
A = [1, 2, 5, -7, 2, 3 ,5]
print(maxset(A))  # Output: [1, 2, 5]
