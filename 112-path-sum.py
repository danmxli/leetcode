from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs_visit(node: Optional[TreeNode], sum: int) -> bool:
        if not node:
            return False
        
        remaining_sum = sum - node.val
        
        if remaining_sum == 0 and (not node.left) and (not node.right):
            return True
        
        return dfs_visit(node.left, remaining_sum) or dfs_visit(node.right, remaining_sum)

    return dfs_visit(root, targetSum)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(hasPathSum(root, 5))