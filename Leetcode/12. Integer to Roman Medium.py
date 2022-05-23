class Solution:
    """With dictionary"""
    def intToRoman(self, num: int) -> str:
        ans = ''
        dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'}
        nums = [i for i in dict.keys()]
        n = -1
        while num != 0:
            if num - nums[n] >= 0:
                num -= nums[n]
                ans += str(dict[nums[n]])
            else:
                n -= 1
        return ans
