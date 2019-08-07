# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def traverse(self, root):
        self.allNodes = []
        self.counter = 0
        self.__traverse(root)

    def __traverse(self, cur):
        if cur is None or self.counter == self.k:
            return
        self.__traverse(cur.left)
        if self.counter == self.k:
            return
        self.allNodes.append(cur)
        self.counter += 1
        self.__traverse(cur.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.traverse(root)
        return self.allNodes[-1].val
