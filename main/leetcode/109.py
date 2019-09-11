# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        if not nums:
            return None
        self.nums = nums
        return self.__helper(0, len(nums) - 1)

    def __helper(self, lo, hi):
        if lo > hi:
            return None
        if lo == hi:
            return TreeNode(self.nums[lo])
        mid = (lo + hi) // 2 + (1 if (lo + hi) % 2 == 1 else 0)
        mid_node = TreeNode(self.nums[mid])
        mid_node.left = self.__helper(lo, mid - 1)
        mid_node.right = self.__helper(mid + 1, hi)
        return mid_node