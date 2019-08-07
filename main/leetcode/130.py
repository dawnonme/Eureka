from queue import Queue


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row, col = len(board), len(board[0])
        dp = [[True] * col for _ in range(row)]
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(row):
            for j in range(col):
                if not dp[i][j]:
                    continue
                if board[i][j] == 'X':
                    dp[i][j] = False
                elif board[i][j] == 'O' and (i == 0 or i == row - 1 or j == 0
                                             or j == col - 1):
                    dp[i][j] = False
                    q = Queue()
                    q.put((i, j))
                    while not q.empty():
                        I, J = q.get()
                        for nei in neighbors:
                            new_i, new_j = I + nei[0], J + nei[1]
                            if (0 <= new_i < row
                                    and 0 <= new_j < col) and dp[new_i][
                                        new_j] and board[new_i][new_j] == 'O':
                                dp[new_i][new_j] = False
                                q.put((new_i, new_j))

        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if dp[i][j]:
                    board[i][j] = 'X'
