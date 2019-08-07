class Solution:
    def threeSum(self, nums):
        # O(n^2)
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        last = nums[0]
        for fst in range(len(nums) - 2):  # fix the first element
            if fst > 0 and last == nums[fst]:
                continue
            sec = fst + 1
            trd = len(nums) - 1
            while sec < trd:
                sum_of_three = nums[fst] + nums[sec] + nums[trd]
                if sum_of_three == 0:
                    res.append([nums[fst], nums[sec], nums[trd]])
                    sec += 1
                    trd -= 1
                    while sec < trd and nums[sec] == nums[sec - 1]:
                        sec += 1
                    while sec < trd and nums[trd] == nums[trd + 1]:
                        trd -= 1
                elif sum_of_three > 0:
                    trd -= 1
                else:
                    sec += 1
            last = nums[fst]
        return res
