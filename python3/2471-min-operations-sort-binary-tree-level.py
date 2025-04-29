from collections import deque, defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition:
# bfs to create a list of nodes for each level
# for each level, sort the nodes and count the operations
# return the total operations

class Solution:

    def countSortOperations(self, nums: list[int]):
        operations = 0
        nums = nums.copy()
        sorted_nums = sorted(nums)
        # build a mapping of nodes to list index
        idx_table = {node: i for i, node in enumerate(nums)}
        
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                operations += 1

                # swap
                correct_index = idx_table[sorted_nums[i]]
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

                idx_table[nums[i]] = i
                idx_table[nums[correct_index]] = correct_index

        return operations

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])

        # for each level, sort the nodes and count the operations
        operations = 0

        while queue:
            level_store = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level_store.append(curr.val)

                # neighbor exploration
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            print(level_store)
            operations += self.countSortOperations(level_store)

        return operations

# example: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
root = TreeNode(1, TreeNode(4, TreeNode(7), TreeNode(6)), TreeNode(3, TreeNode(8), TreeNode(5, TreeNode(9), TreeNode(10))))
print(Solution().minimumOperations(root))