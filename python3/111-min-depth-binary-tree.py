from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        def dfsHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return float('inf')
            
            if not root.left and not root.right:
                return 1
                
            left = dfsHelper(root.left)
            right = dfsHelper(root.right)
            
            return min(left, right) + 1
        
        return dfsHelper(root)

        
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.minDepth(root))