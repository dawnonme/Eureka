# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque
        tree_list = deque([root, root])
        while tree_list:
            t1 = tree_list.popleft()
            t2 = tree_list.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            tree_list.append(t1.left)
            tree_list.append(t2.right)
            tree_list.append(t1.right)
            tree_list.append(t2.left)
        return True

    def is_symmetric_recursion(self, root):
        def helper(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and helper(t1.right, t2.left) and helper(t1.left, t2.right)
        return helper(root, root)
