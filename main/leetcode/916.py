from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        B = list(map(Counter, B))
        cnt = Counter()
        for b in B:
            cnt |= b

        res = []
        for a in A:
            ca = Counter(a)
            if all(ca[i] >= cnt[i] for i in cnt):
                res.append(a)

        return res