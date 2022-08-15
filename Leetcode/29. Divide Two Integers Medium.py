class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        sign = 1

        def ans(x):
            if x > 2147483647:
                return 2147483647
            if x < -2147483648:
                return -2147483648
            return x

        if dividend < 0 and divisor < 0:
            dividend *= -1
            divisor *= -1
        elif dividend < 0 and divisor > 0:
            dividend *= -1
            sign *= -1
        elif dividend > 0 and divisor < 0:
            divisor *= -1
            sign *= -1
        if divisor == 1:
            return ans(dividend * sign)
        if dividend < divisor or not dividend:
            return count

        temp = divisor
        while dividend >= divisor:
            tempcount = 1
            while temp + temp < dividend:
                temp = temp + temp
                tempcount = tempcount + tempcount
            dividend -= temp
            temp = divisor
            count += tempcount
        return ans(count * sign)
