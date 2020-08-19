class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]

        opt = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            opt[i] = suffix_sum[i] - opt[i + 1]
            gen = (j for j in range(i + 1, i + 3) if j < n)
            for j in gen:
                if j < n:
                    opt[i] = max(opt[i], suffix_sum[i] - opt[j + 1])

        ret = "Tie"
        if opt[0] * 2 > suffix_sum[0]:
            ret = "Alice"
        elif opt[0] * 2 < suffix_sum[0]:
            ret = "Bob"
        return ret
