# Validate Binary Search Tree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.topo = []
        self.inorder_traversal(root)
        for i in range(len(self.topo) - 1):
            if self.topo[i] >= self.topo[i + 1]:
                return False
        return True

    def inorder_traversal(self, cur):
        if not cur:
            return

        self.inorder_traversal(cur.left)
        self.topo.append(cur.val)
        self.inorder_traversal(cur.right)

    def recursion_method(self, root):
        def helper(cur, lower=float('-inf'), upper=float('inf')):
            if not cur:
                return True

            if cur.val >= upper or cur.val <= lower:
                return False

            return helper(cur.left, lower, cur.val) and helper(
                cur.right, cur.val, upper)

        return helper(root)

    def iteration_method(self, root):
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
