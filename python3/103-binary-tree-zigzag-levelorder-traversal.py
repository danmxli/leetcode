# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition, use double-ended queue
# level order traversal, alternating between FIFO and LIFO element removal
from typing import Optional, List
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = deque([root])
        level = 0
        answer = []

        while q:
            l = len(q)
            level_nodes = []
            
            for _ in range(l):
                curr = q.popleft()
                level_nodes.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            if len(level_nodes) > 0:
                if level % 2 != 0:
                    level_nodes.reverse()
                answer.append(level_nodes)
                level += 1                

        return answer
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.zigzagLevelOrder(root))