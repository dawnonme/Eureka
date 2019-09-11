# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ''' Stack
        '''
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        res, power, carry_out = [], 0, 0
        while stack1 or stack2:
            num1 = stack1.pop() if stack1 else 0
            num2 = stack2.pop() if stack2 else 0
            num = num1 + num2 + carry_out
            if num >= 10:
                num -= 10
                carry_out = 1
            else:
                carry_out = 0
            res = [num] + res
        if carry_out == 1:
            res = [1] + res

        head = ListNode(res[0])
        cur = head
        for i in range(1, len(res)):
            cur.next = ListNode(res[i])
            cur = cur.next
        return head