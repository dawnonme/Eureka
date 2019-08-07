# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        stack = [root]
        in_idx = len(inorder) - 1

        for i in range(len(postorder) - 2, -1, -1):
            node = TreeNode(postorder[i])
            prev = None
            while stack and stack[-1].val == inorder[in_idx]:
                prev = stack.pop()
                in_idx -= 1
            if prev:
                prev.left = node
            else:
                stack[-1].right = node
            stack.append(node)

        return root