class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        neighbors = [
            (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for i in range(row):
            for j in range(col):
                count = 0
                for nei in neighbors:
                    new_i, new_j = i + nei[0], j + nei[1]
                    if new_i < 0 or new_i >= row:
                        continue
                    if new_j < 0 or new_j >= col:
                        continue
                    if board[new_i][new_j] > 0:
                        count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = -1
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
