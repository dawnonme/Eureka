class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import defaultdict

        table = defaultdict(int)

        for row in matrix:
            if row[0] == 0:
                table[tuple(row)] += 1
            else:
                table[tuple(1 - col for col in row)] += 1

        return max(table.values())