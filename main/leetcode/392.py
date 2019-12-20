class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if not s:
            return True

        dp = [0] * len(t)
        if s[0] == t[0]:
            dp[0] = 1

        for i in range(1, len(t)):
            if s[dp[i - 1]] == t[i]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
            if dp[i] == len(s):
                return True

        return False

    def is_subsequence(self, s, t):
        if not s:
            return True
        idx = 0
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
                if idx == len(s):
                    return True
        return False
