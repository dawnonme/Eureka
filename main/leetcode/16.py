class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        from math import inf
        nums.sort()
        res = 0
        min_dis = inf
        last = nums[0]
        for fst in range(len(nums) - 2):
            if fst > 0 and last == nums[fst]:
                continue
            sec = fst + 1
            trd = len(nums) - 1
            while sec < trd:
                sum_of_3 = nums[fst] + nums[sec] + nums[trd]
                dis = sum_of_3 - target
                abs_dis = abs(dis)
                if abs_dis < min_dis:
                    min_dis = abs_dis
                    res = sum_of_3
                if dis > 0:
                    trd -= 1
                    while sec < trd and nums[trd] == nums[trd + 1]:
                        trd -= 1
                elif dis < 0:
                    sec += 1
                    while sec < trd and nums[sec] == nums[sec - 1]:
                        sec += 1
                else:
                    return res
            last = nums[fst]
        return res