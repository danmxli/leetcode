from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# unoptimized intuition:
# flatten the bst using in-order traversal

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list = []
        val_list = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return

            dfs(root.left)
            node_list.append(root)
            val_list.append(root.val)
            dfs(root.right)

        dfs(root)
        val_list = sorted(val_list)

        for i in range(len(val_list)):
            node_list[i].val = val_list[i]
        return
    
root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)

sol = Solution()
print(sol.recoverTree(root))