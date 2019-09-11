class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        lo = ans = 0
        hi = 1
        decreasing = False

        while hi < len(A):
            if A[hi] > A[lo]:
                prev = A[hi]
                hi += 1
                while hi < len(A) and A[hi] > prev:
                    prev = A[hi]
                    hi += 1
                if hi < len(A) and A[hi] < prev:
                    while hi < len(A) and A[hi] < prev:
                        prev = A[hi]
                        hi += 1
                    ans = max(ans, hi - lo)
                lo = hi - 1 

            else:
                hi += 1
                lo += 1

        return ans
                

