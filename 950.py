class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque

        index = deque(range(len(deck)))
        ret =  [0] * len(deck)

        deck.sort()
        for c in deck:
            ret[index.popleft()] = c
            if index:
                index.append(index.popleft())

        return ret