from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        ...

        def dfsHelper(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            if not root1 and not root2:
                return
            elif not root1:
                return root2
            elif not root2:
                return root1

            mergedRoot = TreeNode(root1.val + root2.val)
            mergedRoot.left = dfsHelper(root1.left, root2.left)
            mergedRoot.right = dfsHelper(root1.right, root2.right)

            return mergedRoot
        
        return dfsHelper(root1, root2)

