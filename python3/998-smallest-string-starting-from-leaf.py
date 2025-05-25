from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition: bfs approach
# each item stores current node and current string
# the corresponding char is chr(node_val + ord('a'))

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = ""
        q = deque([(root, chr(root.val + ord('a')))])

        while q:
            (curr_node, curr_ans) = q.popleft()

            # leaf node condition
            if not curr_node.left and not curr_node.right:
                if ans == "":
                    ans = curr_ans
                else:
                    ans = min(ans, curr_ans)

            if curr_node.left:
                q.append((curr_node.left, chr(curr_node.left.val + ord('a')) + curr_ans))
            if curr_node.right:
                q.append((curr_node.right, chr(curr_node.right.val + ord('a')) + curr_ans))

        return ans
    
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

sol = Solution()
print(sol.smallestFromLeaf(root))