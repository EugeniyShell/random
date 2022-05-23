class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            y = (int(str(''.join(i for i in str(x)[::-1]))))
        else:
            y = -int(str(''.join(i for i in str(x)[:0:-1])))
        return (y if -2 ** 31 < y < 2 ** 31 else 0)
