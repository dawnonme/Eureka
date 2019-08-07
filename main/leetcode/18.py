class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        last_i1 = nums[0]
        for i1 in range(len(nums) - 3):
            if i1 > 0 and last_i1 == nums[i1]:
                continue
            last_i2 = nums[i1 + 1]
            for i2 in range(i1 + 1, len(nums) - 2):
                if i2 > i1 + 1 and last_i2 == nums[i2]:
                    continue
                i3 = i2 + 1
                i4 = len(nums) - 1
                while i3 < i4:
                    sum_of_4 = nums[i1] + nums[i2] + nums[i3] + nums[i4]
                    if sum_of_4 == target:
                        res.append([nums[i1], nums[i2], nums[i3], nums[i4]])
                        i3 += 1
                        i4 -= 1
                        while i3 < i4 and nums[i3] == nums[i3 - 1]:
                            i3 += 1
                        while i3 < i4 and nums[i4] == nums[i4 + 1]:
                            i4 -= 1
                    elif sum_of_4 > target:
                        i4 -= 1
                    else:
                        i3 += 1
                last_i2 = nums[i2]
            last_i1 = nums[i1]
        return res