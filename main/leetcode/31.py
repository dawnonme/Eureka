class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the first decreasing element from the end to the beginning
        last, target = float('-inf'), -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= last:
                last = nums[i]
            else:
                target = i
                break
        