# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        def helper(lo, hi):
            if lo > hi:
                return [None]
            if lo == hi:
                return [TreeNode(lo)]

            tree_list = []

            for i in range(lo, hi + 1):
                left = helper(lo, i - 1)
                right = helper(i + 1, hi)

                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left, node.right = l, r
                        tree_list.append(node)

            return tree_list

        return helper(1, n)
