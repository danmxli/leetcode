from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_levelorder_traversal(root: TreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def traversal_builder(root: TreeNode):
    
    preorder_arr = []
    inorder_arr = []

    def dfs_preorder_traversal(root: TreeNode):
        if not root:
            return
        preorder_arr.append(root.val)
        dfs_preorder_traversal(root.left)
        dfs_preorder_traversal(root.right)

    def dfs_inorder_traversal(root: TreeNode):
        if not root:
            return
        dfs_inorder_traversal(root.left)
        inorder_arr.append(root.val)
        dfs_inorder_traversal(root.right)
    
    dfs_preorder_traversal(root)
    dfs_inorder_traversal(root)
    return{"preorder": preorder_arr, "inorder": inorder_arr}

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(traversal_builder(root))