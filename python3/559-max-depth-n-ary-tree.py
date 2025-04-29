from typing import List, Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = deque([root])
        depth = 0

        if not root:
            return 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not curr.children:
                    continue
                for child in curr.children:
                    queue.append(child)
        return depth

sol = Solution()
print(sol.maxDepth(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))