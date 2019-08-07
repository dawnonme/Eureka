from collections import defaultdict


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int],
                    p4: List[int]) -> bool:
        euc_dis = lambda m, n: (m[0] - n[0])**2 + (m[1] - n[1])**2
        d12 = euc_dis(p1, p2)
        d34 = euc_dis(p3, p4)
        d23 = euc_dis(p3, p2)
        d14 = euc_dis(p1, p4)
        d24 = euc_dis(p2, p4)
        d13 = euc_dis(p1, p3)

        cnt = defaultdict(int)
        cnt[d12] += 1
        cnt[d34] += 1
        cnt[d23] += 1
        cnt[d14] += 1
        cnt[d24] += 1
        cnt[d13] += 1

        if len(cnt) == 2:
            k = list(cnt.keys())
            v = list(cnt.values())
            if min(k) * 2 == max(k) and max(v) == 4 and min(v) == 2:
                return True
        return False
