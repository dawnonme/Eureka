class Solution:
    '''
    Define F(n) = Length of the longest sequence from 0 ~ n.
    '''

    def length_of_LIS_recursion(self, nums):
        ''' Brute Force: Time( O(2^n) ), Space( O(n) )
        Use recursion. Main idea is:
        F(n) = F(n - 1) + 1 = A if include nums[n]
             = F(n - 1) = B if not include nums[n]
        Then F(n) = max(A, B).
        '''

        def _length_of_LIS_recursion(nums, cur, prev):
            if cur == len(nums):
                return 0

            taken = 0
            if nums[cur] > prev:
                taken = 1 + _length_of_LIS_recursion(nums, cur + 1, nums[cur])

            not_taken = _length_of_LIS_recursion(nums, cur + 1, prev)
            return max(taken, not_taken)

        return _length_of_LIS_recursion(nums, 0, -float('inf'))

    def length_of_LIS_memorization_recursion(self, nums):
        ''' Memorization With Recursion: Time( O(n^2) ), Space( O(n^2) )

        '''

    def length_of_LIS_dynamic_programming(self, nums):
        ''' Dynamic Programming: Time( O(n^2) ), Space( O(n) )
        Idea: dp[i] means the longest sequence including i-th element.
        '''
        if not nums:
            return 0

        dp = [1] + [0 for _ in range(len(nums) - 1)]
        res = 1

        for i in range(1, len(nums)):
            max_val = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_val = max(max_val, dp[j])
            dp[i] = max_val + 1
            res = max(res, dp[i])

        return res

    def length_of_LIS_dp_binary_search(self, nums):
        ''' Dynamic Programming + Binary Search: Time( O(nlogn) ), Space( O(n) )

        '''
        from bisect import bisect_left

        def binary_search(A, x, lo=0, hi=None):
            if not hi:
                hi = len(A)
            pos = bisect_left(A, x, lo, hi)
            return pos if pos != hi and A[pos] == x else -1

        # dp = [1] + [0 for _ in range(len(nums) - 1)]
        # res = 0

        # for num in nums:
        #     idx = binary_search(dp, num, 0, res)
        pass  # TODO
