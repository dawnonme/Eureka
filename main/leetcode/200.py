class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        rows, cols = len(grid), len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    stack = []
                    for m, n in neighbors:
                        new_i, new_j = i + m, j + n
                        if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                            continue
                        if grid[new_i][new_j] == '1':
                            stack.append((new_i, new_j))

                    while len(stack) > 0:
                        ii, jj = stack.pop()
                        grid[ii][jj] = '#'
                        for m, n in neighbors:
                            new_i, new_j = ii + m, jj + n
                            if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                                continue
                            if grid[new_i][new_j] == '1':
                                stack.append((new_i, new_j))

        return num_islands