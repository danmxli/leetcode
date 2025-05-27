from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# intuition
# flatten unsorted values into a list

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:        
        node_list = []
        
        def traverse(head: Optional[ListNode]):
            if not head:
                return
            node_list.append(head.val)
            traverse(head.next)

        traverse(head)

        # find the next greater for each item in node_list
        n = len(node_list)
        ans = [0 for _ in range(n)]

        # base case
        if n == 1:
            return ans
        
        # decreasing property, iterate through elements in reverse
        stack = []
        for i in reversed(range(n)):
            while stack and stack[-1] <= node_list[i]:
                stack.pop()

            # next top of the stack has the next greater value of val
            if stack:
                ans[i] = stack[-1]

            stack.append(node_list[i])

        return ans
    
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(5)

sol = Solution()
print(sol.nextLargerNodes(head))