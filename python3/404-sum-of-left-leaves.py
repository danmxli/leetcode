from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        sum = [0]

        def dfs(root: Optional[TreeNode], isLeft: bool):
            if not root:
                return
            if not root.left and not root.right and isLeft:
                sum[0] += root.val

            dfs(root.left, True)
            dfs(root.right, False)

        dfs(root, False)
        return sum[0]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.sumOfLeftLeaves(root))