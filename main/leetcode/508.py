# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        from collections import Counter

        self.max_freq = 0
        self.counter = Counter()
        self.__helper(root)
        return [k for k, v in self.counter.items() if v == self.max_freq]

    def __helper(self, node):
        if not node:
            return 0

        left_tree_sum = self.__helper(node.left)
        right_tree_sum = self.__helper(node.right)

        this_tree_sum = left_tree_sum + right_tree_sum + node.val
        self.counter[this_tree_sum] += 1
        self.max_freq = max(self.max_freq, self.counter[this_tree_sum])
        return this_tree_sum