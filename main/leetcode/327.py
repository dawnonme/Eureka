class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)
        self.lower, self.upper = lower, upper
        return self.merge_sort_and_count(self.sums, 0, len(self.sums) - 1)

    def merge_sort_and_count(self, sums, lo, hi):
        if lo >= hi:
            return 0
        cnt = 0
        mid = (lo + hi) // 2

        cnt += self.merge_sort_and_count(sums, lo, mid)
        cnt += self.merge_sort_and_count(sums, mid + 1, hi)

        i = j = mid

        for k in range(lo, mid):
            while i <= hi and self.sums[i] - self.sums[k] < self.lower:
                i += 1
            while j <= hi and self.sums[j] - self.sums[k] <= self.upper:
                j += 1
            cnt += j - i

        sums[lo:hi + 1] = sorted(sums[lo:hi + 1])

        return cnt