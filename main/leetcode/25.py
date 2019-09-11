''' Reverse Nodes in k-Group '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head

        idx, cur, prev = 1, head, dummy_node
        while cur:
            if idx < k:
                cur = cur.next
                idx += 1
            else:
                remain = last = cur.next
                p = prev.next
                prev.next = cur
                prev = p
                while True:
                    tmp = p.next
                    p.next = last
                    last = p
                    p = tmp
                    if p == remain:
                        break
                cur = remain
                idx = 1
        return dummy_node.next
