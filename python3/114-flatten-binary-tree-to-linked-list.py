from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            node_list.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        
        # handle base cases
        if len(node_list) == 0:
            return None
        if len(node_list) == 1:
            node_list[0].left = None
            node_list[0].right = None
            return
        
        # build the linked list
        for i in range(len(node_list)-1):
            node_list[i].left = None
            node_list[i].right = node_list[i+1]
        
        node_list[len(node_list)-1].left = None
        node_list[len(node_list)-1].right = None