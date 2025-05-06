from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # edge case
        if not root:
            return []
        
        ans = []
        q = deque([root])
        
        while q:
            l = len(q)
            level_nodes = []
            
            for _ in range(l):
                curr = q.popleft()
                level_nodes.append(curr.val)

                # adjacent exploration
                for child in curr.children:
                    q.append(child)

            if len(level_nodes) > 0:
                ans.append(level_nodes)

        return ans