# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        prev, cur = dummy_node, head
        idx = 1
        while cur:
            if idx == m:
                last = None
                reverse_p = cur
                while idx < n + 1:
                    if idx == n:
                        prev.next = reverse_p
                    tmp = reverse_p.next
                    reverse_p.next = last
                    last = reverse_p
                    reverse_p = tmp
                    idx += 1
                cur.next = reverse_p
                break
            else:
                cur = cur.next
                prev = prev.next
                idx += 1

        return dummy_node.next
