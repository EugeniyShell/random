"""2 way - bruteforce with loop and BS"""

'''class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        import math

        nok = (a * b) // math.gcd(a, b)
        res = {x * a for x in range(1, (nok // a) + 1)}
        res = list(res.union({y * b for y in range(1, (nok // b) + 1)}))
        res.sort()
        x = n % len(res)
        y = n // len(res)
        ans = nok * y
        if x:
            ans += res[x-1]
        return ans if ans < 10**9+7 else ans % (10**9+7)'''


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        a, b = min(a, b), max(a, b)
        lcm = self.getLCM(a, b)
        base_lcm = lcm // a + lcm // b - 1
        cnt_lcm = n // base_lcm

        n %= base_lcm
        l = 0
        r = a * n

        while l <= r:
            m = (l + r) // 2
            if n <= m // a + m // b:
                r = m - 1
            else:
                l = m + 1

        return (l + cnt_lcm * lcm) % (10 ** 9 + 7)

    def getLCM(self, a, b):
        return a // self.getGCD(a, b) * b

    def getGCD(self, a, b):
        if b == 0:
            return a

        return self.getGCD(b, a % b)