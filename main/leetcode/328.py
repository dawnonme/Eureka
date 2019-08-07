# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd, even = head, head.next
        fst, snd = head, head.next
        cur_idx = 1
        last_odd = None

        while True:
            if fst and snd:
                if cur_idx % 2 != 0:
                    last_odd = fst
                else:
                    last_odd = snd
                fst.next = snd.next
                fst = snd
                snd = snd.next
                cur_idx += 1
            elif fst:
                if cur_idx % 2 != 0:
                    fst.next = even
                else:
                    last_odd.next = even
                break
        return odd