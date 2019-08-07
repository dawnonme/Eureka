# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        head = self.merge_sort(head)
        return head

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        left, right = self.split_list(head)

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        res = self.merge_list(left, right)
        return res

    def merge_list(self, head1, head2):
        if not head1 and not head2:
            return None
        if not head1:
            return head2
        if not head2:
            return head1

        if head1.val <= head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next
        cur = head

        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1:
            cur.next = head1
        elif head2:
            cur.next = head2

        return head

    def split_list(self, head):
        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        prev.next = None
        return head, slow
