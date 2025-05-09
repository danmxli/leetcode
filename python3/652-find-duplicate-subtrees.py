from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition
# dfs traversal, generate string repr of subtree rooted at current node, store count in hashtable
# if found, append that node to the answer list

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        table = defaultdict(int)
        ans = []
        
        def preOrder(root: Optional[TreeNode]) -> str:
            if not root:
                return "."
            
            # build the string repr
            val = str(root.val)
            left = preOrder(root.left)
            right = preOrder(root.right)
            repr = val + "," + left + "," + right
            
            table[repr] += 1
            if table[repr] == 2:
                ans.append(root)

            return repr

        preOrder(root)
        return ans
    
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.findDuplicateSubtrees(root))