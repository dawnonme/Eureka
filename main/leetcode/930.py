class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        indices = [i for i in range(len(A)) if A[i] == 1]
        ans = 0

        if S == 0:
            indices = [-1] + indices + [len(A)]
            for i in range(1, len(indices)):
                num_zero = indices[i] - indices[i - 1] - 1
                ans += (1 + num_zero) * num_zero // 2
            return ans

        lo = 0
        hi = S - 1

        while hi < len(indices):
            last = (indices[lo] -
                    indices[lo - 1]) if lo > 0 else indices[lo] + 1
            next = (
                indices[hi + 1] -
                indices[hi]) if hi < len(indices) - 1 else len(A) - indices[hi]
            ans += last * next
            lo += 1
            hi += 1

        return ans