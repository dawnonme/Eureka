class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = {}
        last_remainder = 0

        for i in range(len(nums)):
            if last_remainder not in cache:
                cache[last_remainder] = i
            last_remainder += nums[i]
            if k != 0:
                last_remainder %= k
            if last_remainder in cache and i > cache[last_remainder]:
                return True
        return False