class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sub_arr_sum = {}
        cur_sum = 0
        for i, n in enumerate(nums):
            cur_sum += n
            sub_arr_sum[i] = cur_sum
        for i, n in enumerate(nums):
            if cur_sum == 2 * sub_arr_sum[i] - n:
                return i
        return -1
