class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        from collections import Counter

        MOD = 10**9 + 7

        cnt = Counter(A)
        unique_list = sorted(cnt)
        ans = 0

        for fst in range(len(unique_list)):
            remain = target - unique_list[fst]
            snd, trd = fst, len(unique_list) - 1
            n_fst = cnt[unique_list[fst]]

            while snd <= trd:
                sum23 = unique_list[snd] + unique_list[trd]
                if sum23 > remain:
                    tr(d -= 1
                elif sum23 < remain:
                    snd += 1
                else:
                    n_snd, n_trd = cnt[unique_list[snd]], cnt[unique_list[trd]]
                    if fst == snd == trd:
                        if n_fst >= 3:
                            ans += n_fst * (n_fst - 1) * (n_fst - 2) // 6
                    elif fst == snd < trd:
                        if n_fst >= 2:
                            ans += n_fst * (n_fst - 1) // 2 * n_trd
                    elif fst < snd == trd:
                        if n_snd >= 2:
                            ans += n_fst * n_snd * (n_snd - 1) // 2
                    else:
                        ans += n_fst * n_snd * n_trd
                    trd -= 1
                    snd += 1

        return ans % MOD