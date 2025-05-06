# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition: 1-pass bfs
# queue tracks current node value and its parent
# update curr node value to be (curr level sum of node values) - (curr sibling node values)
# need variables to store the previous values of nodes in the same level
from typing import Optional
from collections import deque

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ...
        # init
        q = deque()
        q.append((root, None))
        row_sum = root.val
        next_row_sum = root.val
        prev_val = None
        prev_parent = None

        while q:
            ...
            l = len(q)
            row_sum = next_row_sum
            next_row_sum = 0

            for i in range(l):
                curr_node, curr_parent = q.popleft()
                
                # compute the cousin sum of the curr node
                cousin_sum = row_sum - curr_node.val
                
                # check if node in same level is NOT a cousin
                if prev_val and prev_parent == curr_parent:
                    cousin_sum -= prev_val
                # EDGE CASE
                if i < l-1 and q[0][1] == curr_parent:
                    cousin_sum -= q[0][0].val

                # prev value updates
                prev_val = curr_node.val
                prev_parent = curr_parent

                # compute the next row sum
                if curr_node.left:
                    next_row_sum += curr_node.left.val
                    q.append((curr_node.left, curr_node))
                if curr_node.right:
                    next_row_sum += curr_node.right.val
                    q.append((curr_node.right, curr_node))

                curr_node.val = cousin_sum

            # reset for next level
            prev_val = None
            prev_parent = None

        return root