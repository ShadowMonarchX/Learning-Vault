# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        curent_value = ListNode(0)
        curent = curent_value
        new_list = []
        for i in lists :
            for j in i :
                new_list.append(j)
        new_list.sort()
        new_list.reverse()

        while new_list :
            curent.next = new_list
            new_list = curent.next
        
        return curent.next
        


lists = [[1,4,5],[1,3,4],[2,6]]
Solution = Solution()
result = Solution.mergeKLists(lists)
print(result)
        