class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        from collections import defaultdict

        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        table = defaultdict(dict)

        def helper(target, idx):
            if target == 0:
                return True
            if target < 0 or idx == len(nums):
                return False
            if idx in table and target in table[idx]:
                return table[idx][target]
            table[idx][target] = helper(
                target - nums[idx], idx + 1) or helper(target, idx + 1)
            return table[idx][target]

        return helper(half, 0)
