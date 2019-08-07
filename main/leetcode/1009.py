class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bN = bin(N)
        max_len = len(bN) - 2
        bMax = '1' * max_len
        Max = int(bMax, 2)
        return Max - N
