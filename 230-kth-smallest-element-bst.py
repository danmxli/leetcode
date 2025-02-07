from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# note: we can optimize this (todo)
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    sorted_nodes = []
    
    def dfs_visit(root: Optional[TreeNode]):
        if not root:
            return
        
        dfs_visit(root.left)
        sorted_nodes.append(root.val)
        dfs_visit(root.right)

    dfs_visit(root)
    return sorted_nodes[k-1]

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

print(kthSmallest(root, 1))