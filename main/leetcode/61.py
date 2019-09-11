# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        cnt, cur = 0, head
        while cur:
            cur = cur.next
            cnt += 1
        if cnt == 0 or cnt == 1:
            return head
        k %= cnt
        if k == 0:
            return head
        p1 = p2 = head
        for _ in range(k):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        tmp = p2.next
        p2.next = None
        p1.next = head
        return tmp
