class Solution:
    """Not clear answer with dictionary and loop"""
    def numberToWords(self, num: int) -> str:
        def rename(num):
            ans = ''
            ones = {
                0: '',
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }

            other = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }

            twos = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            if num >= 100:
                ans += ' ' + ones[num // 100] + ' ' + 'Hundred'
                num = num % 100
            if num >= 20:
                ans += ' ' + twos[num // 10]
            elif 10 <= num < 20:
                ans += ' ' + other[num]
                return ans
            num = num % 10
            if 0 < num < 10:
                ans += ' ' + ones[num]
            else:
                pass
            return ans

        ans = ''
        if not num:
            return 'Zero'
        if num > 999999999:
            ans += rename(num // 1000000000) + ' ' + 'Billion'
            num = num % 1000000000
        if num > 999999:
            ans += rename(num // 1000000) + ' ' + 'Million'
            num = num % 1000000
        if num > 999:
            ans += rename(num // 1000) + ' ' + 'Thousand'
            num = num % 1000
        if num > 0:
            ans += rename(num)

        return ans.lstrip().rstrip()
