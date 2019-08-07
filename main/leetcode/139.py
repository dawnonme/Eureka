# Dynamic Programming

# filled[i] = True means string s in index range [0, i) can be break down by the
# wordDict, then it can be divided intosub-problems. filled[i] = True if there
# exist j < i s.t. filled[j] = True and s[j : i] can be found in wordDict.

import collections


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        filled = [True] + ([False] * len(s))
        word_dict = collections.defaultdict(bool)
        for word in wordDict:
            word_dict[word] = True

        for i in range(len(filled)):
            for j in range(0, i):
                if filled[j] and s[j:i] in word_dict:
                    filled[i] = True

        return filled[-1]
