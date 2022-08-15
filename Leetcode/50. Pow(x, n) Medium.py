class Solution:
    def myPow(self, x: float, n: int) -> float:
        o = 1
        arr = [1 if x=='1' else 0 for x in "{:b}".format(n)]
        if n >= 0:
            for i in arr[:-1]:
                 o = (o * (x ** i)) ** 2
            return o * (x ** arr[-1])
        if n < 0:
            for i in arr[1:-1]:
                 o = (o / (x ** i)) ** 2
            return o / (x ** arr[-1])
