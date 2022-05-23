class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """from itertools import zip_longest
        if numRows < 2:
            return s
        n = numRows
        result = str()
        result = ''.join(s[0::2*(n-1)])
        for i in range(1,n-1):
            result = result + ''.join(x+y for x, y in zip_longest(s[i::2*(n-1)], s[2*(n-1)-i::2*(n-1)], fillvalue=''))
        result = result + ''.join(s[n-1::2*(n-1)])
        return result"""

        if numRows < 2:
            return s
        data = [""] * numRows
        mode = number = 0
        for letters in s:
            if mode == 0:
                data[number] += letters
                number += 1
            else:
                data[number] += letters
                number -= 1

            if number == numRows:
                mode = 1
                number = numRows - 2
            elif number == -1:
                mode = 0
                number = 1
        return ''.join(data)

