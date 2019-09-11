# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        self.sorted_list = ListNode(float('-inf'))
        self.__helper(head)
        return self.sorted_list.next

    def __helper(self, node):
        if not node:
            return
        cur = node
        node = node.next
        p1, p2 = self.sorted_list, self.sorted_list.next
        while True:
            if not p2:
                p1.next = cur
                cur.next = None
                break
            if cur.val > p2.val:
                p1, p2 = p1.next, p2.next
            else:
                p1.next = cur
                cur.next = p2
                break
        self.__helper(node)
