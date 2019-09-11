# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack, res, idx = [], [], 0
        while head:
            while stack and stack[-1][0] < head.val:
                _, index = stack.pop()
                res[index] = head.val
            stack.append((head.val, idx))
            res.append(0)
            idx += 1
            head = head.next
        return res