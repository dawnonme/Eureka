class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ''' Dynamic Programming: Time: O(M * N), Space: O(1)
        '''
        row, col = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        set_num = 1
        for i in range(row):
            if obstacleGrid[i][0] == 1:
                set_num = 0
            obstacleGrid[i][0] = set_num

        set_num = 1
        for j in range(1, col):
            if obstacleGrid[0][j] == 1:
                set_num = 0
            obstacleGrid[0][j] = set_num

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[
                        i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[-1][-1]
