from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # swap the left and right pointers using recursion
        def visit(node: Optional[TreeNode]):
            if not node:
                return
            
            temp = node.left
            node.left = node.right
            node.right = temp

            visit(node.left)
            visit(node.right)
        
        visit(root)
        return root
