class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.__rob(nums[:-1]), self.__rob(nums[1:]))

    def __rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = dp[i - 1] if dp[i - 1] > dp[i - 2] + \
                nums[i] else dp[i - 2] + nums[i]

        return dp[-1]
