class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        from collections import Counter

        if not S:
            return []

        ans = []
        base_window = Counter(S)
        window = Counter()
        lo, hi, cnt = -1, 0, 0

        while hi < len(S):
            base_window[S[hi]] -= 1
            window[S[hi]] += 1
            if base_window[S[hi]] == 0:
                cnt += 1

            if cnt == len(window):
                ans.append(hi - lo)
                lo = hi
                cnt = 0
                window = Counter()

            hi += 1

        return ans

    def partition_labels(self, S: str) -> List[int]:
        ''' Greedy: Time: O(N), Space: O(1)
        '''

        last_idx = {ch: i for i, ch in enumerate(S)}
        ans = []
        lo = hi = 0

        for i, ch in enumerate(S):
            hi = max(hi, last_idx[ch])
            if i == hi:
                ans.append(hi - lo + 1)
                lo = hi + 1

        return ans
