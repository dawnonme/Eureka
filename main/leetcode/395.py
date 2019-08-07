from collections import Counter


class Solution:
    def longest_substring_simple(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(
                    self.longest_substring_simple(t, k) for t in s.split(c))
        return len(s)

    def longest_substring(self, s: str, k: int) -> int:
        ''' Use [26] array: Time ( O(n) )
        '''

        # Counter to count the number of each letters
        counter = Counter(s)

        # start index of the substring
        start = -1

        # max length of the substring
        max_len = 0

        # iterate through the string
        for i in range(len(s)):
            cnt = counter[s[i]]

            # start of the substring
            if cnt >= k and start < 0:
                start = i

            # end of the substring
            elif cnt < k and start >= 0:
                max_len = max(max_len, self.longest_substring(s[start:i], k))
                start = -1
        
        # base case
        if start == 0:
            max_len = len(s)
        elif start > 0:
            max_len = max(max_len, self.longest_substring(s[start:], k))

        return max_len
