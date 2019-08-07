class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if len(board) == 0 or len(board[0]) == 0 or len(word) == 0:
            return False

        self.board, self.word = board, word
        # self.visited = [[False] * len(board[0]) for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs_search(i, j, 0):
                    return True
        return False

    def dfs_search(self, i, j, cur):

        if i < 0 or i >= len(self.board) or j < 0 or j >= len(self.board[0]):
            return False
        if self.word[cur] != self.board[i][j]:
            return False
        if cur == len(self.word) - 1:
            return True
        elif cur >= len(self.word):
            return False

        # self.visited[i][j] = True
        ori = self.board[i][j]
        self.board[i][j] = '-'

        for (ii, ij) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if self.dfs_search(ii, ij, cur + 1):
                # self.visited[i][j] = False
                self.board[i][j] = ori
                return True
        self.board[i][j] = ori
        # self.visited[i][j] = False
        return False