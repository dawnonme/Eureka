# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        from collections import deque

        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        node_dq, depth = deque([root]), 1
        while len(node_dq) > 0:
            if depth == d - 1:
                break
            num_nodes = len(node_dq)
            for _ in range(num_nodes):
                node = node_dq.popleft()
                if node.left:
                    node_dq.append(node.left)

                if node.right:
                    node_dq.append(node.right)
            depth += 1

        for node in node_dq:
            left_child = node.left
            node.left = TreeNode(v)
            node.left.left = left_child

            right_child = node.right
            node.right = TreeNode(v)
            node.right.right = right_child

        return root
