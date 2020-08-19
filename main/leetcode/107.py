# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ret = []

        def helper(node, level):
            if not node:
                return
            if len(ret) <= level:
                ret.append([])
            ret[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 0)

        ret.reverse()

        return ret
