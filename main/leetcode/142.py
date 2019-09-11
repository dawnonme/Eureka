# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        from collections import defaultdict

        table = defaultdict(bool)
        while head:
            if table[head]:
                return head
            table[head] = True
            head = head.next
        return None

    def detect_cycle_2_pointers(self, head):
        if not head or not head.next:
            return None
        
        slow, fast = head.next, head.next.next

        while slow != fast:
            if not slow or not slow.next or not fast or not fast.next:
                return None
            slow, fast = slow.next, fast.next.next

        slow = head

        while slow != fast:
            slow, fast = slow.next, fast.next
        
        return slow
