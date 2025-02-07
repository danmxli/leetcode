from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sorted_nodes = []
        min_diff = float('inf')
        
        def dfs_visit(root: Optional[TreeNode]):
            if not root:
                return
            
            dfs_visit(root.left)
            sorted_nodes.append(root.val)
            dfs_visit(root.right)

        dfs_visit(root)
        
        for i in range(1, len(sorted_nodes)):
            min_diff = min(min_diff, abs(sorted_nodes[i] - sorted_nodes[i-1]))
            
        return min_diff
        
