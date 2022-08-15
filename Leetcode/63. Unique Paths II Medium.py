class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for y in range(m):
            for x in range(n):
                if obstacleGrid[y][x]:
                    obstacleGrid[y][x] = 0
                elif x and y:
                    obstacleGrid[y][x] = obstacleGrid[y - 1][x] + obstacleGrid[y][x - 1]
                elif x:
                    obstacleGrid[y][x] = obstacleGrid[y][x - 1]
                elif y:
                    obstacleGrid[y][x] = obstacleGrid[y - 1][x]
                else:
                    obstacleGrid[y][x] = 1

        return obstacleGrid[m - 1][n - 1]