from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        curr = temp
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            raw_sum = val1 + val2 + carry
            digit_sum = raw_sum % 10
            carry = raw_sum // 10

            # update curr and l1 l2 pointers
            curr.next = ListNode(digit_sum)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return temp.next