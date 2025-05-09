from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # use comma to separate adj nodes
        def preOrder(root: Optional[TreeNode]) -> str:
            if not root:
                return ""
            left = preOrder(root.left)
            right = preOrder(root.right)

            parts = [str(root.val)]
            if left:
                parts.append(left)
            if right:
                parts.append(right)

            return ",".join(parts)
        
        return preOrder(root)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        node_values = [int(x) for x in data.split(",") if x]
        if not node_values:
            return None
        index = [0] # python: mutable value for recursion

        def build(min_val, max_val):
            if index[0] == len(node_values):
                return None
            
            val = node_values[index[0]]

            if not (min_val < val < max_val):
                return None
            
            node = TreeNode(val)
            index[0] += 1
            node.left = build(min_val, val)
            node.right = build(val, max_val)
            return node

        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans