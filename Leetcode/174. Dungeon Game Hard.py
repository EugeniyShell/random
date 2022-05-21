class Solution:
    """Variant of DP solution"""
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        for y in range(m - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                if x == n - 1 and y == m - 1:
                    dungeon[y][x] = max(1, 1 - dungeon[y][x])
                elif x == n - 1:
                    dungeon[y][x] = max(1, dungeon[y + 1][x] - dungeon[y][x])
                elif y == m - 1:
                    dungeon[y][x] = max(1, dungeon[y][x + 1] - dungeon[y][x])
                else:
                    dungeon[y][x] = max(1, min(dungeon[y][x + 1] - dungeon[y][x], dungeon[y + 1][x] - dungeon[y][x]))

        return dungeon[0][0]
