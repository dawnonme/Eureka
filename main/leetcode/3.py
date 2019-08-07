class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        lo = hi = 0
        maxLen = 1
        slidingWindow = {}
        for i, char in enumerate(s):
            if char not in slidingWindow or (char in slidingWindow and slidingWindow[char] < lo):
                hi = i
                slidingWindow[char] = i
            else:
                maxLen = max(maxLen, hi - lo + 1)
                lo = slidingWindow[char] + 1
                hi = i
                slidingWindow[char] = i
        return max(maxLen, hi - lo + 1)
