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

    # Constant space solution
    def isPalindromeV2(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # Find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        dummy_node = ListNode(-1)
        while slow:
            tmp_node = slow.next
            slow.next = dummy_node.next
            
            dummy_node.next = slow
            slow = tmp_node
        
        left_node = head
        right_node = dummy_node.next
            
        while right_node:
            if left_node.val != right_node.val:
                return False
            
            left_node = left_node.next
            right_node = right_node.next
        return True