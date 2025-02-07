from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        node_queue = deque([root])
        depth_queue = deque([1])

        while node_queue:
            
            node = node_queue.popleft()
            curr_depth = depth_queue.popleft()

            if node.left:
                node_queue.append(node.left)
                depth_queue.append(curr_depth + 1)
            if node.right:
                node_queue.append(node.right)
                depth_queue.append(curr_depth + 1)
            
        return curr_depth