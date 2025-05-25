from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition: convert into sorted list
# apply two sum logic to list

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ...
        nums = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
        
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        
        dfs(root)

        table = defaultdict(int)
        for i in range(len(nums)):
            complement = k - nums[i]
            if complement in table:
                return True
            else:
                table[nums[i]] = i

        return False