'''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] # dp logic

        return dp[-1][-1]'''

'''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1,m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
            print(dp)
        return dp[n-1]'''

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)