class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        hi = lo = 0
        cur_sum = 0
        ans = float('inf')

        while hi < len(nums):
            cur_sum += nums[hi]
            
            while cur_sum >= s:
                ans = min(ans, hi - lo + 1)
                cur_sum -= nums[lo]
                lo += 1
            hi += 1
        
        return ans if ans != float('inf') else 0