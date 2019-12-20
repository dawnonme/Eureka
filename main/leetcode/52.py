'''
N-Queen Problem II
'''


class Solution:
    def totalNQueens(self, n: int) -> int:
        from collections import defaultdict

        res = 0

        # initial queen board with no queen being placed
        queen = [['.'] * n for _ in range(n)]

        # check if 2 queens are in the same columns
        occupied_cols = defaultdict(bool)

        # check if 2 queens attack each other in diagonal
        occupied_diagonals_pos = defaultdict(bool)
        occupied_diagonals_neg = defaultdict(bool)

        def backtracking(row):
            if row == n:
                nonlocal res
                res += 1
                return
            for col in range(n):
                pos, neg = row + col, row - col
                if occupied_cols[col] or occupied_diagonals_pos[pos] or occupied_diagonals_neg[neg]:
                    continue

                # set occupied
                occupied_cols[col] = True
                occupied_diagonals_pos[pos] = True
                occupied_diagonals_neg[neg] = True
                queen[row][col] = 'Q'

                backtracking(row + 1)

                # remove occupied (backtrack to the previous states)
                occupied_cols[col] = False
                occupied_diagonals_pos[pos] = False
                occupied_diagonals_neg[neg] = False
                queen[row][col] = '.'

        backtracking(0)
        return res
