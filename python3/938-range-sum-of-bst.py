from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ans = [0]
        
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            dfs(root.left)
            # add to answer if value is in inclusive range
            if low <= root.val <= high:
                ans[0] += root.val
            dfs(root.right)

        # in-order traversal
        dfs(root)
        return ans[0]