from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        # add () when there is an empty node on left and right node exists.
        # preorder traversal
        def dfsHelper(root: Optional[TreeNode]) -> str:
            if not root:
                return ""
            
            s = str(root.val)

            if root.left or root.right:
                next_l = dfsHelper(root.left)
                s += "(" + next_l + ")"
        
            if root.right:
                next_r = dfsHelper(root.right)
                s += "(" + next_r + ")"

            return s

        return dfsHelper(root)