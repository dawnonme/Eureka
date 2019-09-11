# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        new_head = nodes[0]
        new_head.next = nodes[-1]
        cur = new_head.next
        for i in range(1, len(nodes) // 2):
            cur.next = nodes[i]
            cur.next.next = nodes[len(nodes) - 1 - i]
            cur = cur.next.next

        if len(nodes) % 2 == 1:
            cur.next = nodes[len(nodes) // 2]
            cur.next.next = None
        else:
            cur.next = None

        return new_head