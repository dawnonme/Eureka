"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        res, stack = head, []
        cur = res
        if cur.next:
            stack.append(cur.next)
        if cur.child:
            stack.append(cur.child)
            cur.child = None

        while stack:
            ele = stack.pop()
            cur.next = ele
            ele.prev = cur
            if ele.next:
                stack.append(ele.next)
            if ele.child:
                stack.append(ele.child)
                ele.child = None
            cur = cur.next
        return res

    def flatten_recursion(self, head):
        def dfs(head):
            if not head:
                return None

            prev = None
            # iterate through current list
            while head:
                # if there is child list for current head
                if not head.child:
                    prev = head
                    head = head.next
                    continue

                # recursively flatten the child dll first
                flattened_list = dfs(head.child)
                # put the flattened list in between current node and next node
                n = head.next
                head.next = head.child
                head.child.prev = head
                head.child = None
                flattened_list.next = n
                if n:
                    n.prev = flattened_list

                prev = flattened_list
                head = n

            return prev

        dfs(head)
        return head