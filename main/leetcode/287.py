class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]  # every time forward by 1 step
            fast = nums[nums[fast]]  # every time forward by 2 steps
            if slow == fast:  # there will be a time for the 2 to be the same, which is the entrance of the loop
                break

        # slow and fast can be just the same index, so we can't just return, we need another loop
        p1 = nums[0]
        p2 = slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1