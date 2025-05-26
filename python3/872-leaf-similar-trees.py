from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def find_sequence(root: Optional[TreeNode]):
            s = []
            def dfs(root: Optional[TreeNode]):
                if not root:
                    return
                if not root.left and not root.right:
                    s.append(root.val)
                dfs(root.left)
                dfs(root.right)

            dfs(root)
            return s
        
        s1 = find_sequence(root1)
        s2 = find_sequence(root2)

        return s1 == s2