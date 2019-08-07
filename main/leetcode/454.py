from collections import defaultdict


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int],
                     D: List[int]) -> int:
        two_sum = defaultdict(int)
        for a in A:
            for b in B:
                two_sum[a + b] += 1
        count = 0
        for c in C:
            for d in D:
                remainder = -(c + d)
                if remainder in two_sum:
                    count += two_sum[remainder]

        return count