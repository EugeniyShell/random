class Solution:
    """Two variants"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        """sub = str()
        string = set(s)
        for i in range(len(s)):
            temp = s[i]
            try:
                index = s.index(temp, i + 1)
            except:
                index = len(s)
            if len(sub) > len(s[i + 1:index]):
                continue
            else:
                for n in range(len(s[i + 1:index])):
                    if s[i + 1:][n] not in temp:
                        temp += s[i + 1:][n]
                    elif s[i + 1:][n] in temp:
                        break
            if len(sub) == len(string):
                return len(sub)
            if len(temp) == len(string):
                return len(temp)
            if len(temp) > len(sub):
                sub = temp

        return len(sub)"""

        max_l = 0
        my_str = ""
        for x in s:
            if x not in my_str:
                my_str += x
            else:
                if len(my_str) > max_l:
                    max_l = len(my_str)
                my_str = my_str[my_str.find(x) + 1:]
                my_str += x
        max_l = max(max_l, len(my_str))
        return max_l
