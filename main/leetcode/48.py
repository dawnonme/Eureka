class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        self._rotate(0, len(matrix))

    def _rotate(self, start, length):
        if length == 0 or length == 1:
            return

        end = len(self.matrix) - start - 1

        for i in range(start, end):
            tmp1 = self.matrix[i][end]
            self.matrix[i][end] = self.matrix[start][i]
            tmp2 = self.matrix[end][-1 - i]
            self.matrix[end][-1 - i] = tmp1
            tmp1 = self.matrix[-1 - i][start]
            self.matrix[-1 - i][start] = tmp2
            self.matrix[start][i] = tmp1

        self._rotate(start + 1, length - 2)
