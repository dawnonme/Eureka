class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alex = lee = 0
        alex_turn = True
        while piles:
            if piles[0] > piles[-1]:
                stone = piles.pop(0)
            else:
                stone = piles.pop()
            if alex_turn:
                alex += stone
            else:
                lee += stone
        return alex > lee