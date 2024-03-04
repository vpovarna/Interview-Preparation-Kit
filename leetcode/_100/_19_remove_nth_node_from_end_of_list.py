# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = self.get_length(head)
        
        # create a new list with a dummy node at the beginning
        dummy = ListNode(0)
        dummy.next = head
        
        # create a tmp node 
        node = dummy
        
        pos = 0
        while pos < len -n:
            node  = node.next
            pos +=1
        
        node.next = node.next.next
        
        return dummy.next
    
    def get_length(self, head: ListNode) -> int:
        len  = 0
        tmp = head
        
        while tmp is not None:
            tmp = tmp.next
            len += 1

        return len