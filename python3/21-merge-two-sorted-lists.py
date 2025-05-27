from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# naive approach

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def toList(head: Optional[ListNode]):
            node_list = []
            def traverse(head: Optional[ListNode]):
                if not head:
                    return
                node_list.append(head)
                traverse(head.next)
            
            traverse(head)
            return node_list

        space1 = toList(list1)
        space2 = toList(list2)

        space = sorted((space1 + space2), key=lambda item: item.val)

        if len(space) == 0:
            return None
        if len(space) == 1:
            return space[0]
        
        for i in range(len(space)-1):
            space[i].next = space[i+1]
        
        space[len(space)-1].next = None
        return space[0]