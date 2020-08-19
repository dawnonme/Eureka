# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ret = []

        def helper(node, cur_path):
            if not node:
                return
            if not node.left and not node.right:
                cur_path += "->" + str(node.val)
                ret.append(cur_path[2:])
                return
            cur_path += "->" + str(node.val)
            helper(node.left, cur_path)
            helper(node.right, cur_path)

        helper(root, "")
        return ret
