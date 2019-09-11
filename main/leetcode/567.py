class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        if len(s1) > len(s2):
            return False

        lo = hi = 0
        window = Counter(s1)

        while hi < len(s2):
            ch = s2[hi]
            if window[ch] > 0:
                window[ch] -= 1
                hi += 1
            else:
                window[s2[lo]] += 1
                lo += 1

            if hi - lo == len(s1):
                return True

        return False

    def check_inclusion(self, s1, s2):
        from collections import Counter

        if len(s1) > len(s2):
            return False

        window = Counter(s1)
        a = ord('a')
        cnt = 0

        for i in range(26):
            if window[chr(a + i)] == 0:
                cnt += 1

        for i in range(len(s1)):
            window[s2[i]] -= 1
            if window[s2[i]] == 0:
                cnt += 1
            elif window[s2[i]] == -1:
                cnt -= 1

        for i in range(1, len(s2) - len(s1) + 1):
            if cnt == 26:
                return True

            window[s2[i - 1]] += 1
            if window[s2[i - 1]] == 0:
                cnt += 1
            elif window[s2[i - 1]] == 1:
                cnt -= 1

            window[s2[i + len(s1) - 1]] -= 1
            if window[s2[i + len(s1) - 1]] == 0:
                cnt += 1
            elif window[s2[i + len(s1) - 1]] == -1:
                cnt -= 1

        return cnt == 26