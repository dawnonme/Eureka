class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res, self.nums = [[]], nums
        self._subsets(0)
        return self.res

    def _subsets(self, cur):
        if cur == len(self.nums):
            return

        cur_num = self.nums[cur]
        ori_len = len(self.res)
        for i in range(ori_len):
            new_subset = self.res[i][:]
            new_subset.append(cur_num)
            self.res.append(new_subset)

        self._subsets(cur + 1)
