class Solution:
    def intervalIntersection(self, A: List[List[int]],
                             B: List[List[int]]) -> List[List[int]]:
        a = b = 0
        ans = []

        while a < len(A) and b < len(B):
            lo = max(A[a][0], B[b][0])
            hi = min(A[a][1], B[b][1])

            if lo <= hi:
                ans.append([lo, hi])

            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1

        return ans
