class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        coordinate = lambda one_D_idx: (one_D_idx // col, one_D_idx % col)
        
        def binary_search():
            lo = 0
            hi = row * col - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                i, j = coordinate(mid)
                if matrix[i][j] > target:
                    hi = mid - 1
                elif matrix[i][j] < target:
                    lo = mid + 1
                else:
                    return mid
            return -1
        return binary_search() >= 0




    