from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dsa: delete node in a bst
# recursively search the tree for target node
# case 1: no child
# case 2: one child
# case 3: more than one child

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # tree traversal to find key node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # deletion cases
        else:
            # one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # multiple recursive children: find the successor from right subtree
            curr = root.right
            while curr.left:
                curr = curr.left
            
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)
        
        return root