from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # build array from linkedlist
        nums = []
        def traverse(head: Optional[ListNode]):
            # base case
            if not head:
                return
            nums.append(head.val)
            traverse(head.next)
        
        traverse(head)

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