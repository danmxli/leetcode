from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs approach
from collections import deque, defaultdict

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        ...
        q = deque([root])

        while q:
            l = len(q)
            level_nodes = defaultdict(int)
            for _ in range(l):
                curr = q.popleft()
                if curr.left:
                    level_nodes[curr.left.val] = curr.val
                    q.append(curr.left)
                if curr.right:
                    level_nodes[curr.right.val] = curr.val
                    q.append(curr.right)
            
            if len(level_nodes.keys()) <= 0:
                continue

            if (x in level_nodes and y in level_nodes) and (level_nodes[x] != level_nodes[y]):
                return True

        # exhaused all levels
        return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

sol = Solution()
print(sol.isCousins(root, 4,5))