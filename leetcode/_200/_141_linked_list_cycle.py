from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        visited = set()
        cur_node = head
        
        while cur_node:
            if cur_node in visited:
                return True
            visited.add(cur_node)
            cur_node = cur_node.next

        
        return False

    
    def hasCycleTwoPointer(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
        return True