# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        self.res = []
        self._nextLargerNodes(head)
        return self.res

    def _nextLargerNodes(self, node):
        if not node:
            self.res.append(0)
            return node.val
        next_larger = 

