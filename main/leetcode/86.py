# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        larger_eq = []
        smaller = []
        cur = head
        while cur:
            if cur.val < x:
                smaller.append(cur)
            else:
                larger_eq.append(cur)
            cur = cur.next
        nodes = smaller + larger_eq
        head = nodes[0]
        cur = head
        for i in range(1, len(nodes)):
            cur.next = nodes[i]
            cur = cur.next
        cur.next = None
        return head