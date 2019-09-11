''' Merge k Sorted Lists '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq

        if not lists:
            return None

        heap = [(ls.val, i) for i, ls in enumerate(lists) if ls]

        if not heap:
            return None

        heapq.heapify(heap)
        _, first_idx = heapq.heappop(heap)
        head = lists[first_idx]
        lists[first_idx] = lists[first_idx].next
        if lists[first_idx]:
            heapq.heappush(heap, (lists[first_idx].val, first_idx))
        cur = head

        while heap:
            _, idx = heapq.heappop(heap)
            cur.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
            cur = cur.next
        cur.next = None
        
        return head