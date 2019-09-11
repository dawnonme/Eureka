class WordDictionary:
    '''
    Word dictionary, support insert and search operations.
    '''

    class TrieNode:
        '''
        Trie Node for the trie tree.
        '''

        def __init__(self):
            self.children = {}
            self.end_of_word = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = self.TrieNode()
            cur = cur.children[ch]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.__dfs_search(self.root, word)

    def __dfs_search(self, node, word):
        if not word:
            return node.end_of_word
        first = word[0]
        if first != '.':
            if first not in node.children:
                return False
            return self.__dfs_search(node.children[first], word[1:])
        for ch, child in node.children.items():
            if self.__dfs_search(child, word[1:]):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)