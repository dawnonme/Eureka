class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False

        dp = [1] + [0 for _ in range(len(nums) - 1)]
        res = 1

        for i in range(1, len(nums)):
            max_val = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_val = max(max_val, dp[j])

                dp[i] = max_val + 1
                res = max(res, dp[i])
                if res >= 3:
                    return True

        return False

    def increasing_triplet(self, nums):
        if not len(nums):
            return False

        fst, snd = nums[0], float('inf')

        for i in range(1, len(nums)):
            if nums[i] > snd:
                return True
            elif snd > nums[i] > fst:
                snd = nums[i]
            elif nums[i] < fst:
                fst = nums[i]
        return False