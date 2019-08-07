# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = defaultdict(list)
        self._levelOrder(root, 0)
        return list(self.res.values())

    def _levelOrder(self, cur_node, cur_level):
        if not cur_node:
            return

        self.res[cur_level].append(cur_node.val)
        self._levelOrder(cur_node.left, cur_level + 1)
        self._levelOrder(cur_node.right, cur_level + 1)
