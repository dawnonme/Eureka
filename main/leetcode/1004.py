class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start = 0
        max_len = 0
        for i, num in enumerate(A):
            if num == 0:
                if K > 0:
                    K -= 1
                else:
                    max_len = max(max_len, i - start)
                    while start < len(A) and A[start] == 1:
                        start += 1
                    start += 1
        return max(max_len, i - start + 1)