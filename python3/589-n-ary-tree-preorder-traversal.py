from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfsHelper(root: Optional[Node]):
            if not root:
                return
            ans.append(root.val)
            for child in root.children:
                dfsHelper(child)

        dfsHelper(root)
        return ans