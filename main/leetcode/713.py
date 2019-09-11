class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0

        lo = hi = 0
        cur_prod = 1
        ans = 0

        while hi < len(nums):
            cur_prod *= nums[hi]

            if cur_prod >= k and hi != lo:
                while cur_prod >= k and lo < len(nums):

                    ans += (hi - lo)
                    cur_prod //= nums[lo]
                    lo += 1

            hi += 1

        ans += ((hi - lo) + 1) * (hi - lo) // 2 if hi > lo else 0

        return ans