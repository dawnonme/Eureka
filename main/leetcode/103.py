# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        dq = [root]
        rev = False
        cur_level = 0
        num_pop = 1
        num_app = 0

        while len(dq) > 0:
            temp = []
            while num_pop > 0:
                node = dq.pop()
                res[cur_level].append(node.val)
                num_pop -= 1
                if rev:
                    if node.right:
                        temp.append(node.right)
                        num_app += 1
                    if node.left:
                        temp.append(node.left)
                        num_app += 1

                else:
                    if node.left:
                        temp.append(node.left)
                        num_app += 1
                    if node.right:
                        temp.append(node.right)
                        num_app += 1

            num_pop = num_app
            num_app = 0
            cur_level += 1
            dq = temp
            rev = not rev

        return list(res.values())

    def recursive_method(self, root):
        self.res = defaultdict(list)
        self._recursive_method(root, 0, False)
        return list(self.res.values())

    def _recursive_method(self, node, level, rev):
        if not node:
            return

        self.res[level].append(node.val)

        if rev:
            self._recursive_method(node.left, level + 1, False)
            self._recursive_method(node.right, level + 1, False)

        else:
            self._recursive_method(node.right, level + 1, True)
            self._recursive_method(node.left, level + 1, True)
