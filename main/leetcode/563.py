# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ret = 0

        def helper(node):
            nonlocal ret
            if not node:
                return 0

            left_sum = helper(node.left)
            right_sum = helper(node.right)

            ret += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val

        helper(root)

        return ret

