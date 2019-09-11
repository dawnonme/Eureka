from collections import Counter


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def get_neighbors(self, word):
        neighbors = []
        for i in range(len(word)):
            neighbors.append(word[:i] + '*' + word[i + 1:])
        return neighbors

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.words = set(dict)
        self.count = Counter(nei for word in dict
                             for nei in self.get_neighbors(word))

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return any(self.count[nei] > 1
                   or self.count[nei] == 1 and word not in self.words
                   for nei in self.get_neighbors(word))


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)