from math import log


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        if self.row * self.col == 0:
            raise ValueError("Invalid matrix!")
        self.is_square = (self.row == self.col)

    def __getitem__(self, i, j):
        return self.matrix[i][j]

    def show_mat(self):
        for i in range(self.row):
            print(self.matrix[i])

    def mat_mul_naive(self, m):
        if self.col != m.row:
            raise ArithmeticError("Dimensions of matrices mismatch!")

        res = Matrix([[0] * m.col for _ in range(self.row)])
        for i in range(res.row):
            for j in range(res.col):
                for k in range(self.col):
                    res[i][j] += self[i][k] * m[k][j]
        return res

    def 
