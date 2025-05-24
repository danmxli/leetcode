from typing import List, Optional

# Definition for a binary tree node.
# intuition: build the path through function arguments

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(root: Optional[TreeNode], path) -> str:
            if not root:
                return
            
            path += str(root.val) + "->"
            if not root.left and not root.right:
                # remove the final "->"
                p_list = list(path)
                p_list.pop()
                p_list.pop()

                path = "".join(p_list)
                ans.append(path)
                return

            dfs(root.left, path)
            dfs(root.right, path)

        dfs(root, "")
        return ans
    
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(sol.binaryTreePaths(root))