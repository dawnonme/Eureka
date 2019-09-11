# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self._constructMaximumBinaryTree(nums, 0, len(nums) - 1)

    def _constructMaximumBinaryTree(self, nums, lo, hi):
        if lo > hi:
            return None
        elif lo == hi:
            return TreeNode(nums[lo])
        val, idx = self.find_max_and_idx(nums, lo, hi)
        root = TreeNode(val)
        root.left = self._constructMaximumBinaryTree(nums, lo, idx - 1)
        root.right = self._constructMaximumBinaryTree(nums, idx + 1, hi)
        return root

    def find_max_and_idx(self, nums, lo, hi):
        top_val, top_idx = float('-inf'), -1
        for i in range(lo, hi + 1):
            if nums[i] > top_val:
                top_val, top_idx = nums[i], i
        return top_val, top_idx