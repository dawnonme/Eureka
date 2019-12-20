class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        Dynamic Programming: O(N^2)
        '''
        if not nums:
            return []
        nums.sort()
        dp = [None] * len(nums)
        dp[0] = [nums[0]]

        for i in range(1, len(nums)):
            max_subset = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    max_subset = max(max_subset, dp[j][:], key=len)
            max_subset.append(nums[i])
            dp[i] = max_subset

        return max(dp, key=len)

    def largest_divisible_subset(self, nums):
        '''
        Better: O(N * sqrt(x)) where x is the number in nums
        '''
        from math import sqrt

        nums.sort()
        l, prev = {}, {}  # length, previous number(largest divisor in nums)
        max_l, end_number = 0, None

        for i in nums:
            tmp_l, tmp_prev = 0, None
            for j in range(1, 1 + int(sqrt(i))):
                if i % j == 0:
                    tmp = i // j
                    if tmp in prev and l[tmp] > tmp_l:
                        tmp_l, tmp_prev = l[tmp], tmp
                    if j in prev and l[j] > tmp_l:
                        tmp_l, tmp_prev = l[j], j

            tmp_l += 1
            prev[i], l[i] = tmp_prev, tmp_l

            if tmp_l > max_l:
                max_l, end_number = tmp_l, i

        ans = []
        while end_number is not None:
            ans.append(end_number)
            end_number = prev[end_number]

        return ans
