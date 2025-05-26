from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        node_list = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            dfs(root.left)
            node_list.append(root.val)
            dfs(root.right)

        dfs(root)
        
        # no second min if only root exists
        if len(node_list) == 1:
            return -1
        
        node_list = sorted(node_list)
        minimum = min(node_list)

        for i in range(len(node_list)):
            if node_list[i] > minimum:
                return node_list[i]
        return -1