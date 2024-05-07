from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = self.reverse(head)

        carry = 0
        previous, current = None, reversed_list

        while current:
            new_value = current.val * 2 + carry
            current.val = new_value % 10
            carry = 1 if new_value > 9 else 0
            previous, current = current, current.next

        if carry > 0:
            previous.next = ListNode(carry)

        result_list = self.reverse(reversed_list)
        return result_list

    def reverse(self, node: ListNode) -> ListNode:
        previous, current = None, node

        while current:
            next_node = current.next
            current.next = previous
            previous, current = current, next_node

        return previous
