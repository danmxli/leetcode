from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition: frequency count

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        table = defaultdict(int)

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            
            # update node value frequency
            if root.val not in table:
                table[root.val] = 1
            else:
                table[root.val] += 1
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        
        mode_val = max([table[key] for key in table])
        ans = []
        for key in table:
            if table[key] == mode_val:
                ans.append(key)

        return ans