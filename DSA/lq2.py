
# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode(0)
        current = new_list
        while head:
            current.next = head
            head = current.next
        count = 0
        mid = 0
        print(current)
        while current:
            count += 1
            current = current.next
        print(count)
        if count % 2 == 0 :
            mid = count / 2
        else :
            mid = count // 2
            mid += 1
        print(mid)
        node_delete = mid
        if new_list == node_delete:
            return new_list.next

        current_node = new_list
        while current_node.next:
            if current_node.next == node_delete:
                current_node.next = current_node.next.next
                return head
            current_node = current_node.next

        return new_list.next
Solution = Solution()
head = [1,3,4,7,1,2,6]
result = Solution.deleteMiddle(head)
print(result)

# Def