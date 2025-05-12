from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        ...
        # bfs
        # if you encounter NULL, return False if nodes appear to the right
        
        q = deque([root])
        nullEncountered = False

        while q:
            curr = q.popleft()

            if curr.left:
                if nullEncountered:
                    return False
                q.append(curr.left)
            else:
                nullEncountered = True
            
            if curr.right:
                if nullEncountered:
                    return False
                q.append(curr.right)
            else:
                nullEncountered = True

        return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

sol = Solution()
print(sol.isCompleteTree(root))