from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path[:])
                return
            
            for i in range(start, target + 1):
                if i > target:
                    break
                path.append(i)
                backtrack(i, target - i, path, result)
                path.pop()

        result = []
        backtrack(1, target, [], result)
        return result
        out = []
        for comb in result:
            if not any(item in candidates for item in comb):
                out.append(comb)
        return out

            

candidates = [2,3,5]
target = 8   
Solution = Solution()
result = Solution.combinationSum(candidates,target)
print(result)