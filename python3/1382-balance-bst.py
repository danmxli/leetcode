from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# properties of bst: 
# left child <= curr
# right child > curr

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ...
        # build sorted list from root using in-order traversal
        sortedList = []
        def inOrder(root: Optional[TreeNode]):
            if not root:
                return
            
            inOrder(root.left)
            sortedList.append(root.val)
            inOrder(root.right)

        # construct new balanced tree from the sorted list
        # intuition: recursive binary search
        def buildTree(nums, low, high) -> Optional[TreeNode]:
            # base case
            if low > high:
                return None
            
            # create the root from the value of the "median index"
            mid = (low + high) // 2
            root = TreeNode(nums[mid])

            # build the children from the left and right sides
            root.left = buildTree(nums, low, mid-1)
            root.right = buildTree(nums, mid+1, high)

            return root

        inOrder(root)
        return buildTree(sortedList, 0, len(sortedList) - 1)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
sol = Solution()
print(sol.balanceBST(root))
