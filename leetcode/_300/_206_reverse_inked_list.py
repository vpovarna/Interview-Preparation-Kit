from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        current_node = head
        
        while current_node:
            # save the current node
            next_node = current_node.next
            current_node.next = dummyNode.next
            
            dummyNode.next = current_node
            current_node = next_node

        return dummyNode.next

    
if __name__ == "__main__":
    print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
        