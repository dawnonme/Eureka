from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda: None)
        self.end_of_word = False


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie_root = TrieNode()
        for prefix in dict:
            cur = trie_root
            for ch in prefix:
                if not cur.children[ch]:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.end_of_word = True
        split_sentence = sentence.split()

        for i in range(len(split_sentence)):
            ori = split_sentence[i]
            cur = trie_root
            for j in range(len(ori)):
                if cur.end_of_word:
                    split_sentence[i] = ori[:j]
                    break
                if cur.children[ori[j]]:
                    cur = cur.children[ori[j]]
                else:
                    break
        ans = ''
        for word in split_sentence:
            ans += word + ' '
        return ans[:-1]