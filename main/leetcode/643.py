class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lo = 0
        hi = k - 1
        amount = sum(nums[lo:hi + 1])
        max_sum = amount
        while hi < len(nums) - 1:
            amount -= nums[lo]
            lo += 1
            hi += 1
            amount += nums[hi]
            max_sum = max(max_sum, amount)
        return max_sum / k