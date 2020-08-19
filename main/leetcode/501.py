# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        cur_val, cur_ctr, max_ctr = root.val, 0, 0

        def process_node(node):
            nonlocal cur_val, cur_ctr, max_ctr
            if node.val == cur_val:
                cur_ctr += 1
            else:
                cur_ctr = 1
                cur_val = node.val
            max_ctr = max(max_ctr, cur_ctr)

        def process_node_res(node):
            nonlocal cur_val, cur_ctr, max_ctr
            if node.val == cur_val:
                cur_ctr += 1
            else:
                cur_ctr = 1
                cur_val = node.val
            if cur_ctr == max_ctr:
                res.append(node.val)

        def inorder(node, method):
            if node is None:
                return
            inorder(node.left, method)
            method(node)
            inorder(node.right, method)

        inorder(root, process_node)
        print(max_ctr)
        cur_val, cur_ctr = root.val, 0
        res = []
        inorder(root, process_node_res)
        return res
