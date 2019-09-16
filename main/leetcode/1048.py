class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        from collections import defaultdict

        words.sort(key=lambda word: -len(word))
        lookup = set(words)
        dic = defaultdict(int)
        ans = 1

        for word in words:
            for i in range(len(word)):
                child = word[:i] + word[i + 1:]
                if child in lookup:
                    dic[child] = max(dic[child], dic[word] + 1)
                    ans = max(ans, dic[child] + 1)
        return ans
