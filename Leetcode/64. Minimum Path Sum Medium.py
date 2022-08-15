class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for y in range(m):
            for x in range(n):
                if not x and not y:
                    pass
                elif not x:
                    grid[y][x] += grid[y - 1][x]
                elif not y:
                    grid[y][x] += grid[y][x - 1]
                else:
                    grid[y][x] += min(grid[y][x - 1], grid[y - 1][x])

        return grid[m - 1][n - 1]