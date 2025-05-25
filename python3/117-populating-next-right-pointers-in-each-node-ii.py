from collections import deque

"""
Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        q = deque([root])

        while q:
            l = len(q)
            level_nodes = []
            for _ in range(l):
                curr = q.popleft()
                
                if curr.left:
                    q.append(curr.left)
                    level_nodes.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    level_nodes.append(curr.right)
            
            if len(level_nodes) > 1:
                for i in range(len(level_nodes)-1):
                    level_nodes[i].next = level_nodes[i+1]

        return root