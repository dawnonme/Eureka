class Solution:
    def original_sol(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        diff = [nums[0]]
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i - 1])

        dp = [1] * len(diff)
        dp[0] = 1
        dp[1] = 2 if nums[1] != nums[0] else 1
        for i in range(2, len(diff)):
            max_dp = 1 if nums[i] != nums[0] else float('-inf')
            for j in range(1, i):
                if diff[i] * diff[j] < 0:
                    max_dp = max(max_dp, dp[j])
            dp[i] = 1 + max_dp
        return max(dp)

    def dynamic_programming(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # i-th element is at down position or up position
        up, down = [0] * len(nums), [0] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                # make i at up position
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                # make i at down position
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
        # plus 1 because the first element is not counted
        return max(down[-1], up[-1]) + 1

    def linear_dynamic_programming(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # i-th element is at down position or up position
        up, down = [0] * len(nums), [0] * len(nums)
        up[0], down[0] = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up[i], down[i] = down[i - 1] + 1, down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i], down[i] = up[i - 1], up[i - 1] + 1
            else:
                up[i], down[i] = up[i - 1], down[i - 1]
        return max(up[-1], down[-1])

    def greedy(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        prev_diff = nums[1] - nums[0]
        cnt = 2 if prev_diff != 0 else 1
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                cnt += 1
                prev_diff = diff
        return cnt
