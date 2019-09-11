class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_num, cnt, idx = float('-inf'), 0, 0

        while idx < len(nums):
            if cur_num != nums[idx]:
                cur_num = nums[idx]
                cnt = 0
            cnt += 1
            if cnt == 3:
                cnt -= 1
                nums.pop(idx)
                idx -= 1
            idx += 1

        return len(nums)