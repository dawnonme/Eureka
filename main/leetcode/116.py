"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        nodes = deque([root])
        while True:
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            nodes[-1].next = None

            if not nodes[0].left:
                return root

            count = len(nodes)
            for i in range(count):
                node = nodes.popleft()
                nodes.append(node.left)
                nodes.append(node.right)
