from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
"""
build the tree by adding nodes in preorder sequence
use inorder position as comparator
 - tree building using inorder position implements divide and conquer, idk how ur supposed to know that from the first try, GG
optimization: use hash table to store index of inorder 
"""

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

    # build the hash table
    table = {}
    for i in range(len(inorder)):
        table[inorder[i]] = i

    def build(pre_i, left, right):
        
        # left and right pointers for divide and conquer
        if left > right:
            return None
        
        # create the root node and increment the preorder index counter
        root_val = preorder[pre_i[0]]
        pre_i[0] += 1
        root = TreeNode(root_val)

        # get index of inorder
        i = table[root_val]

        # divide and conquer
        root.left = build(pre_i, left, i-1)
        root.right = build(pre_i, i+1, right)
        return root

    # init with preorder first index
    pre_i = [0]
    return build(pre_i, 0, len(preorder)-1)

def print_levelorder(root: Optional[TreeNode]):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

t = buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
print_levelorder(t)