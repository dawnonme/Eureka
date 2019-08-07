# find the longest Palindromic sub-string
# Manachar's Algorithm, O(N)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        new_str = '#'
        for char in s:
            new_str += (char + '#')
        lps = [0] * len(new_str)
