from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
the root of a subtree is a valid node in the original tree
all descendants of the root of a subtree are exactly all descendants of the root of the parent tree
"""

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def is_identical(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
                return True
        if not root or not subRoot:
                return False
        return root.val == subRoot.val and is_identical(root.left, subRoot.left) and is_identical(root.right, subRoot.right)
    

    def dfs_visit(root: Optional[TreeNode], target: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == target.val:
            if is_identical(root, target):
                 return True
            
        return dfs_visit(root.left, target) or dfs_visit(root.right, target)

    
    return dfs_visit(root, subRoot)

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subroot = TreeNode(4)
subroot.left = TreeNode(1)
subroot.right = TreeNode(2)

print(isSubtree(root, subroot))
