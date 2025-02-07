from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:

    def dfs_visit(node: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None
        if node.val == p.val or node.val == q.val:
            return node
        """
        after the pre-order traversal, the node is currently the parent of p and q
        THIS IS DUE TO THE CALL STACK BEHAVIOUR
        """
        
        left = dfs_visit(node.left, p, q)
        right = dfs_visit(node.right, p, q)

        if left and right:
            return node
        return left or right
    
    return dfs_visit(root, p, q)
