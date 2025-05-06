from typing import List, Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfsHelper(root: Optional[Node]):
            if not root:
                return
            for child in root.children:
                dfsHelper(child)
            ans.append(root.val)
        
        dfsHelper(root)
        return ans