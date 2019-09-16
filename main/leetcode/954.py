class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        from collections import Counter

        ctr = Counter(A)
        A = sorted(A, key=abs)
        for num in A:
            if ctr[num] == 0:
                continue
            if ctr[2 * num] == 0:
                return False
            ctr[2 * num] -= 1
            ctr[num] -= 1
        return True