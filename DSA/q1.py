from typing import List
from itertools import combinations

class Solution:
    def findMedianSortedArrays(self, nums1: List[int]) ->float:
        combination = list(combinations(nums1, 3))
        lists = []
        for tup in combination:
            lists.append(list(tup))
        filtered_lists = []
        for i in range(len(lists)):
            should_add = True
            for j in range(len(filtered_lists)):
                if set(lists[i]) == set(filtered_lists[j]):
                    should_add = False
                    break 
            if should_add:
                filtered_lists.append(lists[i])

        lists = filtered_lists
        filtered = []
        for lst in lists:
            if sum(lst) == 0:
                filtered.append(lst)
        return filtered
Solution = Solution()
nums1 = [-1,0,1,2,-1,-4]
result = Solution.findMedianSortedArrays(nums1)
print(result)