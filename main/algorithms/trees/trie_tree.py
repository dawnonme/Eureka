''' Trie
Trie is an efficient information reTrieval data structure. Search complexity
can be brought to the length of the key.
'''
from typing import List


class TrieNode:
    '''
    Node for a trie tree. Assume only 26 lower case letters will
    appear in words.
    '''

    def __init__(self):
        # list of children trie nodes
        self.children = [None] * 26

        # is the end of the word
        self.end_of_word = False


class Trie:
    '''
    Trie tree.
    '''

    def __init__(self, root=TrieNode()):
        self.root = root
        self.char_to_idx = lambda ch: ord(ch) - ord('a')

    def insert(self, key):
        cur = self.root
        length = len(key)
        for level in range(length):
            idx = self.char_to_idx(key[level])
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.end_of_word = True

    def search(self, key):
        cur = self.root
        length = len(key)
        for level in range(length):
            idx = self.char_to_idx(key[level])
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur != None and cur.end_of_word