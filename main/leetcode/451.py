class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

        cnt = Counter(s)
        char_list = sorted(cnt, key=lambda ch: (-cnt[ch], ch))

        ans = ''
        for ch in char_list:
            ans += ch * cnt[ch]
        return ans