from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# constraints:
# -100 <= Node.val <= 100

# intuition:
# level order bfs
# queue stores current node and its index in the binary tree
# tree property: left node gets index 2*n, right node gets index 2*n + 1

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        q = deque([(root, 1)])
        
        while q:
            (_, left) = q[0]
            level_size = len(q)

            for i in range(level_size):
                (curr, n) = q.popleft()
                
                if curr.left:
                    q.append((curr.left, 2*n))
                if curr.right:
                    q.append((curr.right, 2*n + 1))

                # compute max width when reached end of level
                if i == level_size - 1:
                    max_width = max(max_width, n - left + 1)

        return max_width
    
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

sol = Solution()
print(sol.widthOfBinaryTree(root))