class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int],
                            worker: List[int]) -> int:
        combined = sorted(zip(difficulty, profit))
        ans = cur = best = 0

        for w in sorted(worker):
            while cur < len(combined) and w >= combined[cur][0]:
                best = max(best, combined[cur][1])
                cur += 1
            ans += best

        return ans