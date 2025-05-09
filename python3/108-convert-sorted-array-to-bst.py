from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # binary search the nums list to build the tree
        def treeBuilder(nums, low, high) -> Optional[TreeNode]:
            # base cases
            if not nums:
                return None
            if low > high:
                return None

            # root node guaranteed to exist
            mid = (low + high) // 2
            root = TreeNode(nums[mid])

            # build the left and right children recursively
            root.left = treeBuilder(nums, low, mid-1)
            root.right = treeBuilder(nums, mid+1, high)

            return root

        return treeBuilder(nums, 0, len(nums)-1)