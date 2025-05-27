from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        
        def traverse(head: Optional[ListNode]):
            if not head:
                return
            node_list.append(head)
            traverse(head.next)
        
        traverse(head)

        # base cases
        if len(node_list) == 1:
            return node_list[0]
        
        middle = math.floor(len(node_list) / 2)
        return node_list[middle]