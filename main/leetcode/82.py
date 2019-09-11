# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy_node = ListNode(float('inf'))
        dummy_node.next = head
        head = dummy_node

        l, m, r = head, head.next, head.next.next
        while r:
            if m.val == r.val:
                while r and r.val == m.val:
                    r = r.next
                l.next = r
                if not r:
                    break
                m = r
                r = r.next
            else:
                l = l.next
                m = m.next
                r = r.next

        return head.next
