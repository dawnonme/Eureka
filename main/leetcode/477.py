# TODO
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        self.nums, self.dis = nums, 0
        self._totalHammingDistance(0)
        return self.dis

    def _totalHammingDistance(self, idx):
        if idx == len(self.nums):
            return
        for i in range(idx):
            self.dis += Solution.hamming_distance(self.nums[idx], self.nums[i])
        self._totalHammingDistance(idx + 1)

    @staticmethod
    def hamming_distance(num1, num2):
        n = num1 ^ num2
        dis = 0
        while n > 0:
            dis += n & 1
            n >>= 1
        return dis