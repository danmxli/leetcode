from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition
# post order traversal
# maintain a non local answer variable

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        ans = [0]

        def dfs(root: Optional[TreeNode]) -> int:
            # base case: |0-0| = 0 when no children
            if not root:
                return 0
            
            # update the tilt of the parent node using the sum of both the left and right children
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            tilt = abs(left_sum - right_sum)
            
            # accumulate the tilt value
            ans[0] += tilt
            
            # update the summation
            return root.val + left_sum + right_sum

        dfs(root)
        return ans[0]
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.findTilt(root))