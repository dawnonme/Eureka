''' Jump Game
Usually, a dynamic programming problem involves 4 steps:
1. Start with the recursive backtracking solution.
2. Optimize by using a memorization table (top-down dp).
3. Remove the need for recursion (bottom-up dp).
4. Apply final tricks to reduce the time / memory complexity.
'''
from enum import Enum


class Index(Enum):
    GOOD = 1  # from this index we can reach the destination
    UNKNOWN = 0  # from this index we don't know the reachability
    BAD = -1  # from this index we can't reach the destination


class Solution:
    def backtracking_method(self, nums):
        ''' Time: O(2^n) Space: O(n) '''

        def _backtracking_method(nums, idx):
            if idx == len(nums) - 1:
                return True

            furthest_idx = min(len(nums) - 1, idx + nums[idx])
            for next_idx in range(furthest_idx, idx, -1):
                if _backtracking_method(nums, next_idx):
                    return True

            return False

        return _backtracking_method(nums, 0)

    def dp_top_down_method(self, nums):
        ''' Time: O(n^2) Space: O(2n) = O(n) '''
        memo = [Index.UNKNOWN] * (len(nums) - 1) + [Index.GOOD]
        return self._dp_top_down_method(nums, 0, memo)

    def _dp_top_down_method(self, nums, idx, memo):
        if memo[idx] != Index.UNKNOWN:
            return True if memo[idx] == Index.GOOD else False

        furthest_idx = min(len(nums) - 1, idx + nums[idx])
        for next_idx in range(furthest_idx, idx, -1):
            if self._dp_top_down_method(nums, next_idx, memo):
                memo[idx] = Index.GOOD
                return True

        memo[idx] = Index.BAD
        return False

    def dp_bottom_up_method(self, nums):
        ''' Time: O(n^2) Space: O(n) '''
        memo = [Index.UNKNOWN] * (len(nums) - 1) + [Index.GOOD]

        for i in range(len(nums) - 2, -1, -1):
            furthest_idx = min(len(nums) - 1, i + nums[i])
            for j in range(i + 1, furthest_idx + 1):
                if memo[j] == Index.GOOD:
                    memo[i] = Index.GOOD
                    break

        return memo[0] == Index.GOOD

    def greedy_method(self, nums):
        ''' Time: O(n) Space: O(1) '''
        last = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last:
                last = i

        return last == 0