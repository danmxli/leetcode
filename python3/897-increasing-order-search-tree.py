from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_list = []
        
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            dfs(root.left)
            node_list.append(root)
            dfs(root.right)
        
        # in-order traversal
        dfs(root)

        # build the new tree
        for i in range(len(node_list)-1):
            node_list[i].left = None
            node_list[i].right = node_list[i+1]
        
        node_list[len(node_list)-1].left = None
        node_list[len(node_list)-1].right = None

        return node_list[0]