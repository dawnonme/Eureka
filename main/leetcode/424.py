class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter

        window = Counter()
        lo = hi = 0
        max_letter_len, ans = 0, 0

        while hi < len(s):

            window[s[hi]] += 1

            max_letter_len = max(max_letter_len, window[s[hi]])

            while hi - lo + 1 - max_letter_len > k:
                window[s[lo]] -= 1
                lo += 1

            ans = max(ans, hi - lo + 1)
            hi += 1
        return ans
