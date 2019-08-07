class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numToRemain = {}
        for i, num in enumerate(nums):
            remain = target - nums[i]
            if num in numToRemain:
                numToRemain[num].append(i)
            else:
                numToRemain[num] = [remain, i]
            if remain in numToRemain:
                if remain == num and len(numToRemain[num]) > 2:
                    return [numToRemain[num][1], numToRemain[num][2]]
                elif remain != num:
                    return [numToRemain[remain][1], numToRemain[num][1]]