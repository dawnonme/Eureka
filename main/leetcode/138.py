"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        table = {}
        cur = head

        while cur:
            new_node = Node(cur.val, None, None)
            table[cur] = new_node
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                table[cur].next = table[cur.next]
            if cur.random:
                table[cur].random = table[cur.random]
            cur = cur.next

        return table[head]
