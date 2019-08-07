class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s == '0' else 1
        if s[0] == '0':
            return 0
        dp = [1] + [0] * (len(s) - 1)
        if s[1] == '0':
            if int(s[:2]) <= 26:
                dp[1] = 1
        else:
            if int(s[:2]) <= 26:
                dp[1] = 2
            else:
                dp[1] = 1

        for i in range(2, len(s)):
            if s[i] == '0':
                if int(s[i - 1:i + 1]) > 26 or s[i - 1] == '0':
                    dp[i] = 0
                else:
                    dp[i] = dp[i - 2]
            else:
                if int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        print(dp)
        return dp[-1]