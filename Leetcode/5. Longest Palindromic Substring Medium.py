class Solution:
    resX = None
    resY = None
    s = None

    def psearch(self, x, y):
        while x > 0 and y < len(self.s):
            if self.s[x - 1] == self.s[y]:
                x -= 1
                y += 1
            else:
                break
        if (y - x) > (self.resY - self.resX):
            self.resX, self.resY = x, y

    def longestPalindrome(self, s: str) -> str:
        self.resX, self.resY = 0, 1
        self.s = s
        for i in range(len(self.s) - 1):
            if i < len(self.s) - 2 and self.s[i] == self.s[i + 2]:
                self.psearch(i, i + 3)
            if self.s[i] == self.s[i + 1]:
                self.psearch(i, i + 2)
        return self.s[self.resX:self.resY]
