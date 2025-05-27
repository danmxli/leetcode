from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        node_list = []

        def traverse(head: Optional[ListNode]):
            if not head:
                return
            if head.val not in seen:
                seen.add(head.val)
                node_list.append(head)
            traverse(head.next)

        traverse(head)

        if len(node_list) == 0:
            return None
        if len(node_list) == 1:
            node_list[0].next = None
            return node_list[0]

        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]
        
        node_list[len(node_list)-1].next = None
        return node_list[0]