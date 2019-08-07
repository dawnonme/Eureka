class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = ""
        for i in range(len(s) - 1):
            left = i - 1
            right = i + 1
            temp = s[i]
            while left >= 0 and right < len(s) and s[left] == s[right]:
                temp = s[left] + temp + s[right]
                left -= 1
                right += 1
            longest = longest if len(longest) > len(temp) else temp
            if s[i] == s[i + 1]:
                left = i - 1
                right = i + 2
                temp = s[i] + s[i + 1]
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    temp = s[left] + temp + s[right]
                    left -= 1
                    right += 1
                longest = longest if len(longest) > len(temp) else temp
        return longest

