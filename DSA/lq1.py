# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curent_value = ListNode(0)
        curent = curent_value

        while list1 and  list2 :
            if list1.val < list2.val :
                curent.next = list1
                list1 = curent.next
            
            else :
                curent.next = list2
                list2 = list2.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return curent_value.next

# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged = solution.mergeTwoLists(list1, list2)

# Print the merged list:
current = merged
while current:
    print(current.val, end=" -> ")
    current = current.next
print("null")
