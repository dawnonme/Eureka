from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_ls = s.split()
        if len(word_ls) != len(pattern):
            return False

        mapping = defaultdict(str)
        exist = defaultdict(bool)

        for i, c in enumerate(pattern):
            if c not in mapping:
                if not exist[word_ls[i]]:
                    exist[word_ls[i]] = True
                    mapping[c] = word_ls[i]
                else:
                    return False
            elif mapping[c] != word_ls[i]:
                return False

        return True

    def word_pattern(self, pattern, s):
        words = s.split(" ")
        if len(pattern) == len(words):
            return len(set(zip(pattern, words))) == len(set(pattern)) == len(
                set(words))
        else:
            return False