class Solution:
    def search_matrix_bfs(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        from queue import Queue

        if not matrix or target < matrix[0][0]:
            return False

        row, col = len(matrix), len(matrix[0])

        q = Queue()
        q.put((0, 0))
        visited = [[False] * col for _ in range(row)]
        visited[0][0] = True

        while not q.empty():
            cur_i, cur_j = q.get()
            if matrix[cur_i][cur_j] == target:
                return True
            elif matrix[cur_i][cur_j] < target:
                if cur_i + 1 < row and not visited[cur_i + 1][cur_j]:
                    q.put((cur_i + 1, cur_j))
                    visited[cur_i + 1][cur_j] = True
                if cur_j + 1 < col and not visited[cur_i][cur_j + 1]:
                    q.put((cur_i, cur_j + 1))
                    visited[cur_i][cur_j + 1] = True
        return False

    def search_matrix_search_condition(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix), len(matrix[0])

        i, j = row - 1, 0

        while 0 <= i < row and 0 <= j < col:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
