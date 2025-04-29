"""
DFS USES RECURSION, AKA "BOTTOM-TO-UP APPROACH (REALLY ANNOYING)"
THREE DIFFERENT WAYS TO DO DFS TRAVERSAL
 - IN-ORDER (left -> dfs_visit -> right) PRINTS SORTED OUTPUT
 - PRE-ORDER (dfs_visit -> left -> right) THE WAY ABDUL BARI TAUGHT DFS
 - POST-ORDER (left -> right -> dfs_visit) AKA THE BOTTOM-TO-UP APPROACH IN THIS TOPIC
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:

    def check(root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # dfs traverse
        left_h = check(root.left)
        if left_h == -1:
            return -1
        right_h = check(root.right)
        if right_h == -1:
            return -1
        
        # unbalanced case
        if abs(left_h - right_h) > 1:
            return -1
        
        # the current height
        return 1 + max(left_h, right_h)

    return check(root) != -1

# Driver
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    # root.left.left.left = TreeNode(8)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    
    print(isBalanced(root))