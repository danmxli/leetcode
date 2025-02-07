from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
starting from root
    left = -inf, right = inf
    evaluate truthness of left < node.val < right

"""

def isValidBST(root: Optional[TreeNode]) -> bool:
    min_val = math.inf * -1
    max_val = math.inf

    def dfs_visit(root: Optional[TreeNode], left, right) -> bool:
        
        if not root:
            return True
        
        if not (left < root.val < right):
            return False
        
        return dfs_visit(root.left, left, root.val) and dfs_visit(root.right, root.val, right)

    return dfs_visit(root, min_val, max_val)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(isValidBST(root))