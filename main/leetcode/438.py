class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = {}

        for c in p:
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

        l = r = 0
        res = []
        count = len(p)

        while r < len(s):
            if s[r] in window:
                window[s[r]] -= 1
                if window[s[r]] >= 0:
                    count -= 1

            if count == 0:
                res.append(l)

            if r - l == len(p) - 1:
                if s[l] in window:
                    if window[s[l]] >= 0:
                        count += 1
                    window[s[l]] += 1
                l += 1

            r += 1

        return res

    def findAnagramsConstantSpace(self, s: str, p: str) -> List[int]: