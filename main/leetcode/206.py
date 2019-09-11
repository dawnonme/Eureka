# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverse_list_recursion(self, head: ListNode) -> ListNode:
        def helper(node, last):
            if not node:
                return None
            tmp = node.next
            node.next = last
            last = node
            if not tmp:
                return node
            node = tmp
            return helper(node, last)

        return helper(head, None)

    def reverse_list_iteration(self, head: ListNode) -> ListNode:
        if not head:
            return head
        last = None
        cur = head
        while True:
            tmp = cur.next
            cur.next = last
            last = cur
            if not tmp:
                return cur
            cur = tmp
        return cur