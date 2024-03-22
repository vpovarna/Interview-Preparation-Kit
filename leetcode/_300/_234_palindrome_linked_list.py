from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        current_node = head
        
        while current_node:
            values.append(current_node.val)
            current_node = current_node.next
        
        left = 0
        right = len(values) -1
        
        while left < right:
            if values[left] != values[right]:
                return False
            
            left +=1
            right -=1

        return True
