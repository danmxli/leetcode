from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hasCycle = [False]
        seen = []
        def traverse(head: Optional[ListNode]):
            if head is None:
                return
            
            if head in seen:
                hasCycle[0] = True
                return
            seen.append(head)
            traverse(head.next)

        traverse(head)
        return hasCycle[0]