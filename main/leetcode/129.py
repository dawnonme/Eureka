# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.__setNumbers(root, 0)
        return self.res

    def __setNumbers(self, node, cur_num):
        if not node:
            return 0

        cur_num *= 10
        cur_num += node.val

        if not node.left and not node.right:
            self.res += cur_num
            return

        self.__setNumbers(node.left, cur_num)
        self.__setNumbers(node.right, cur_num)
