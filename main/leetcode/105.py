# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        in_idx = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            prev = None
            while stack and stack[-1].val == inorder[in_idx]:
                prev = stack.pop()
                in_idx += 1
            if prev:
                prev.right = node
            else:
                stack[-1].left = node
            stack.append(node)

        return root