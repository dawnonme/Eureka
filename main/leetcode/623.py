# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        from collections import deque

        stack, depth = deque([root]), 1
        while stack:
            num_nodes = len(stack)
            for i in range(num_nodes):

        