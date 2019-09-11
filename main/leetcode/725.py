# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        total_num, cur = 0, root
        while cur:
            total_num += 1
            cur = cur.next
        each, remain = divmod(total_num, k)
        num_list = [each + (1 if i < remain else 0) for i in range(k)]
        cur, res, batch_idx, idx = root, [], 1, 0

        while cur:
            if batch_idx == 1:
                res.append(cur)
            if batch_idx == num_list[idx]:
                tmp = cur
                cur = cur.next
                tmp.next = None
                batch_idx = 1
                idx += 1
            else:
                batch_idx += 1
                cur = cur.next
        
        if idx < k:
            res += [None] * (k - idx)

        return res

