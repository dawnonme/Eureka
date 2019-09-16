class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        patterns = {}
        while N > 0:
            key = tuple(cells)
            if key in patterns:
                N %= patterns[key] - N
            patterns[key] = N

            if N == 0:
                break

            for i in range(1, 7):
                if cells[i] == 0:
                    if (cells[i - 1] > 0
                            and cells[i + 1] > 0) or (cells[i - 1] <= 0
                                                      and cells[i + 1] <= 0):
                        cells[i] = -1
                elif cells[i] == 1:
                    if (cells[i - 1] > 0
                            and cells[i + 1] <= 0) or (cells[i - 1] <= 0
                                                       and cells[i + 1] > 0):
                        cells[i] = 2
            cells[0] = 0
            cells[-1] = 0

            for i in range(1, 8):
                if cells[i] == 2:
                    cells[i] = 0
                elif cells[i] == -1:
                    cells[i] = 1

            N -= 1

        return cells
