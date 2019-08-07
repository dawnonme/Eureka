class Solution:
    def dp_method(self, matrix: List[List[int]]) -> List[List[int]]:
        H, W = len(matrix), len(matrix[0])
        res = [[float('inf')] * W for _ in range(H)]

        for i in range(H):
            for j in range(W):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i - 1 >= 0:
                        res[i][j] = min(res[i][j], res[i - 1][j] + 1)
                    if j - 1 >= 0:
                        res[i][j] = min(res[i][j], res[i][j - 1] + 1)

        for i in range(H - 1, -1, -1):
            for j in range(W - 1, -1, -1):
                if i + 1 < H:
                    res[i][j] = min(res[i][j], res[i + 1][j] + 1)
                if j + 1 < W:
                    res[i][j] = min(res[i][j], res[i][j + 1] + 1)

        return res

    def bfs_method(self, matrix):
        H, W = len(matrix), len(matrix[0])
