from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition
# level order traversal, append the rightmost value of each level to the answer list

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        q = deque([root])
        while q:
            l = len(q)
            level_nodes = []
            
            for _ in range(l):
                curr = q.popleft()
                level_nodes.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if level_nodes:
                ans.append(level_nodes[-1])
        
        return ans