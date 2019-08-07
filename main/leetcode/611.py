class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        lo, hi = 0, 2
        res = 0
        last_mid = lo + 1

        while lo < len(nums) - 2:
            for mid in range(last_mid, hi):
                if nums[lo] + nums[mid] > nums[hi]:
                    res += (hi - mid)
                    last_mid = mid
                    break
            hi += 1
            if hi == len(nums):
                lo += 1
                hi = lo + 2
                last_mid = lo + 1

        return res

    def triangle_number(self, nums):
        res = 0
        nums.sort()
        for i in range(len(nums) - 2):
            k = i + 2
            for j in range(i + 1, len(nums) - 1):
                if nums[i] == 0:
                    break
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - 1
        return res

    def triangle_number_two_sum(self, nums):
        res = 0
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            target = nums[i]
            lo = 0
            hi = i - 1
            while lo < hi:
                add = nums[lo] + nums[hi]
                if add > target:
                    res += hi - lo
                    hi -= 1
                else:
                    lo += 1
        return res